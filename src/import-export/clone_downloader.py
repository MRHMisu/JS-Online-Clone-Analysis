import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os


def write_file(filename, fcontent, mode, isprint):
    """
    Write the string content to a file
    copied from
    http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    :param filename: name of the file
    :param fcontent: string content to put into the file
    :param mode: writing mode, 'w' overwrite every time, 'a' append to an existing file
    :return: N/A
    """
    # try:
    file = open(filename, mode)
    file.write(fcontent)
    file.close()

    if isprint:
        print("saved:" + filename)


def delete_file(filename):
    """ delete the file and recreate it
    :param filename: the name of file
    :return: True = succeeded, False = failed
    """
    try:
        os.remove(filename)
    except OSError:
        return False

    return True


def main():
    project = "so-js-clone-analysis"
    file_name = "classifications_" + project + ".csv"
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('serviceAccountKey.json')

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://' + project + '.firebaseio.com/'
    })

    # Get a database reference to our clone pairs.
    ref = db.reference('clones/pairs')
    # download all clone pairs
    clones = ref.get()
    print("total clone pairs: ", len(clones))
    delete_file(file_name)
    # write to a csv file
    content = ""
    for clone in clones:
        content += clone["file1"] + "," + \
                  str(clone["start1"]) + "," + \
                  str(clone["end1"]) + "," + \
                  clone["file2"] + "," + \
                  str(clone["start2"]) + "," + \
                  str(clone["end2"]) + "," + \
                  clone["classification"] + ",\"" + \
                  clone["notes"].replace("\"", "") + "\"\n"

        print(clone['file1'] + " (" + str(clone['start1']) + "," + str(clone['end1']) + ") : " + \
              clone['file2'] + " (" + str(clone['start2']) + "," + str(clone['end2']) + ")")

    write_file(file_name, content, "w", True)


main()
