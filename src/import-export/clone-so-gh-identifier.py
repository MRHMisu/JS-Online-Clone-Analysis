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
line_list = []
so_gh_direction_path = 'so-gh-direction.csv'


def write_lines(contents, path):
    file_writer = open(path, 'w')
    file_writer.writelines(contents)
    file_writer.close()


with open(siamese_filtered_clone_pairs_file) as csvfile:
    count = 0
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        git_snippet_path = row[6]
        git_file_path = github_snippet_base_path + git_snippet_path
        git_code_reader = open(git_file_path, 'r', encoding='utf-8', errors='ignore')
        git_code = git_code_reader.read()
        if stack_overflow_base_path in git_code:
            line_list.append(",".join(row) + '\n')
        git_code_reader.close()
    write_lines(line_list, so_gh_direction_path)
