"""
Export clone_pairs into a JSON file. That can be exported into firebase or MongoDB.

"""

import csv
import json

siamese_filtered_clone_pairs_file = 'all_pairs.csv'
output_json_file = "test-pair.json"
# file header
# serial_no, rank, so_snippet_path, so_start, so_end, length, git_snippet_path, git_start, git_end, length, length_ratio

so_snippet_base_path = '/home/ubuntu/experiment/so-query/'
github_snippet_base_path = '/home/ubuntu/experiment/git-js-corpus/'
json_dictionary = {}
dictionary_list = []


def read_lines(path):
    file_reader = open(path, 'r', encoding='utf-8', errors='ignore')
    lines = file_reader.readlines()
    file_reader.close()
    return lines


with open(siamese_filtered_clone_pairs_file) as csvfile:
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
        so_code = read_lines(so_snippet_base_path + so_snippet_path)
        git_code = read_lines(github_snippet_base_path + git_snippet_path)

        dictionary_list.append({
            '_id': count,
            'file1': so_snippet_path[len(so_snippet_base_path):],
            'start1': so_start,
            'end1': so_end,
            'code1': so_code,
            'file2': git_snippet_path[len(github_snippet_base_path):],
            'start2': git_start,
            'end2': git_end,
            'code2': git_code,
            'classification': '',
            'notes': '',
            'total': 0
        })
        print("Processed row {}".format(count))
        count += 1

    print("Exported {} pairs".format(len(dictionary_list)))
    fcontent = json.dumps(dictionary_list)
    file = open(output_json_file, 'w')
    file.write(fcontent)
    file.close()
