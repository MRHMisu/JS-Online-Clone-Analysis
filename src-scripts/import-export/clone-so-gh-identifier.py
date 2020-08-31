"""
Export clone_pairs thar flow SO->GitHub direction

"""

import csv

siamese_filtered_clone_pairs_file = 'pair-data/SOxGH-without-overlap-0.5-ratio.csv'
# file header
# serial_no, rank, so_snippet_path, so_start, so_end, length, git_snippet_path, git_start, git_end, length, length_ratio

so_snippet_base_path = '/home/ubuntu/experiment/so-query/'
github_snippet_base_path = '/home/ubuntu/experiment/git-js-corpus/'
stack_overflow_base_path = 'https://stackoverflow.com/'
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
        git_snippet_path = row[6]
        git_code = read_lines(github_snippet_base_path + git_snippet_path)
        if stack_overflow_base_path in git_code:
            dictionary_list.append(row)


file = open('so-gh-direction.csv', 'w')
file.writelines(dictionary_list)
file.close()
