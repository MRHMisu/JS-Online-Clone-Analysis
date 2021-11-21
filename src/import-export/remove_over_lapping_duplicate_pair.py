import csv

file_path = "unique_top_rank pairs_len_ratio_0.5.csv"
outputpath = "unique_top_rank_removing_overlapping.csv"
pair_set = {}
with open(file_path) as csvfile:
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
        pair_name = so_snippet_path + "," + git_snippet_path
        pair_set.add(pair_name)


def write_lines(contents, path):
    file_writer = open(path, 'a')
    file_writer.writelines(contents)
    file_writer.close()
