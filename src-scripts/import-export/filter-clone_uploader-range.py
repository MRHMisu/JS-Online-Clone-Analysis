"""
Upload Siamese search result to Firebase database.

"""

import csv
import itertools

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def read_content(path):
    file_reader = open(path, 'r')
    content = file_reader.read()
    file_reader.close()
    return content


def read_line_with_range(file_path, star, end):
    lines = []
    with open(file_path, "r") as text_file:
        for line in itertools.islice(text_file, star, end):
            lines.append(line)
    return '\n'.join(lines)


project_name = 'js-online-clone'

filename = 'pair-data/SOxGH-without-overlap-0.5-ratio.csv'
so_snippet_base_path = '/home/ubuntu/experiment/so-query/'
github_snippet_base_path = '/home/ubuntu/experiment/git-js-corpus/'

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://' + project_name + '.firebaseio.com/'
})
# Get a database reference to our blog.
ref = db.reference('clones/')
pairs_ref = ref.child('pairs')

bigdict = {}
count = 0
rowcount = 0

with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # count how many record we have
    for row in readCSV:
        rowcount += 1

# erase the database, PLEASE DOWNLOAD THE DATABASE BEFORE YOU RUN THIS PROGRAM
pairs_ref.set(dict())

with open(filename) as csvfile:
    count = 0
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        serial_no = row[0]
        rank = row[1]
        so_snippet_path = row[2]
        so_start = row[3]
        so_end = row[4]
        length = row[5]
        git_snippet_path = row[6]
        git_start = row[7]
        git_end = row[8]
        length = row[9]
        length_ratio = row[10]
        classification = ''  # row[11]
        notes = ''  # row[12]

        so_code = read_content(so_snippet_base_path + so_snippet_path)
        git_code = read_line_with_range((github_snippet_base_path + git_snippet_path), int(git_start) - 1, int(git_end))

        bigdict.update({
            count: {
                'file1': so_snippet_path,
                'start1': so_start,
                'end1': so_end,
                'code1': so_code,
                'file2': git_snippet_path,
                'start2': git_start,
                'end2': git_end,
                'code2': git_code,
                'classification': classification,
                'notes': notes,
                'total': rowcount
            }})
        print("Processed row {}".format(count))
        count += 1
        if len(bigdict) > 50:
            pairs_ref.update(bigdict)
            print("Uploaded {} pairs".format(len(bigdict)))
            bigdict = dict()

    # print("size: ", len(bigdict))
    pairs_ref.update(bigdict)
    print("done:", count)
