"""
Upload Siamese search result to Firebase database.

"""

import csv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

project_name = 'so-js-clone-analysis'

filename = 'test_qr_12-08-20_09-52-406-(Unique-Pairs).csv'
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

bigdict = {}
count = 0
rowcount = 0
# erase the database, PLEASE DOWNLOAD THE DATABASE BEFORE YOU RUN THIS PROGRAM
pairs_ref.set(dict())

