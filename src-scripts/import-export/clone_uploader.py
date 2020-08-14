"""
Upload Siamese search result to Firebase database.

"""

import csv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

project_name = 'so-js-clone-analysis'

filename = 'test_qr_12-08-20_09-52-406.csv'
stack_overflow_code_file_path = '/home/ubuntu/experiment/so-query/'
github_code_file_path = '/home/ubuntu/experiment/git-js-corpus/'

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://' + project_name + '.firebaseio.com/'
})

# Get a database reference to our blog.
ref = db.reference('clones/')
pairs_ref = ref.child('pairs')
invested_pairs_ref = ref.child('ipairs')

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
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        clone_method1, start1, end1 = row[0].split('#')
        code_file_path1 =clone_method1.split('.js_')[0] + '.js'
        codefile1 = open(code_file_path1, 'r', encoding='utf-8', errors='ignore')
        code1 = codefile1.read()
        codefile1.close()

        for i in range(1, 2):  # upload distinct stackoverflow code snippets
            # for i in range(1, len(row)):  # upload all stackoverflow <-> github clone pairs (may contain multiple pairs with same stackoverflow snippet)
            clone_method2, start2, end2 = row[i].split('#')
            code_file_path2 = clone_method2.split('.js_')[0] + '.js'
            codefile2 = open(code_file_path2, 'r', encoding='utf-8', errors='ignore')
            code2 = codefile2.read()

            bigdict.update({
                count: {
                    'file1': code_file_path1[len(stack_overflow_code_file_path):],
                    'start1': start1,
                    'end1': end1,
                    'code1': code1,
                    'code1orig': code1,
                    'file2': code_file_path2[len(github_code_file_path):],
                    'start2': start2,
                    'end2': end2,
                    'code2': code2,
                    'code2orig': code2,
                    'classification': '',
                    'notes': '',
                    'total': rowcount
                }
            })
            count += 1
            codefile2.close()

        if len(bigdict) > 100:
            pairs_ref.update(bigdict)
            print("Uploaded {} pairs".format(len(bigdict)))
            bigdict = dict()

    # print("size: ", len(bigdict))
    pairs_ref.update(bigdict)

    print("done:", count)
