"""
Export clone_pairs into a JSON file. That can be exported into firebase or MongoDB.

"""

import csv
import itertools
import json

siamese_filtered_clone_pairs_file = 'pair-data/SOxGH-without-overlap-0.5-ratio.csv'
output_json_file = "SOxGH-without-overlap-0.5-ratio-pair.json"
# file header
# serial_no, rank, so_snippet_path, so_start, so_end, length, git_snippet_path, git_start, git_end, length, length_ratio

so_snippet_base_path = '/home/ubuntu/experiment/so-query/'
github_snippet_base_path = '/home/ubuntu/experiment/git-js-corpus/'
json_dictionary = {}
dictionary_list = []


def get_file_content(path):
    file_reader = open(path, 'r')
    content = file_reader.read()
    file_reader.close()
    return content


def read_line_with_range(file_path, star, end):
    lines = []
    with open(file_path, "r") as text_file:
        for line in itertools.islice(text_file, star, end):
            lines.append(line)


total_pair = 0

with open(siamese_filtered_clone_pairs_file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # count how many record we have
    for row in readCSV:
        total_pair += 1

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
        so_code = get_file_content(so_snippet_base_path + so_snippet_path)
        git_code = read_line_with_range((github_snippet_base_path + git_snippet_path), int(git_start) - 1, int(git_end))

        dictionary_list.append({
            '_id': count,
            'file1': so_snippet_path,
            'start1': so_start,
            'end1': so_end,
            'code1': so_code,
            'file2': git_snippet_path,
            'start2': git_start,
            'end2': git_end,
            'code2': git_code,
            'classification': '',
            'notes': '',
            'total': total_pair
        })
        print("Processed row {}".format(count))
        count += 1

    print("Exported {} pairs".format(len(dictionary_list)))
    fcontent = json.dumps(dictionary_list, indent=4, sort_keys=True)
    file = open(output_json_file, 'w')
    file.write(fcontent)
    file.close()
