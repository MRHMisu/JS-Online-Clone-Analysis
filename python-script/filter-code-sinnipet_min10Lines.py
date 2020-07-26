import csv
import sys


def filter_code_snippet_by_loc(path, output):
    code_snippet_min_10_lines = []
    code_snippet_min_10_lines.append("answer_id,question_id,loc,code_snippet" + '\n')
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            loc = int(row[3])
            if loc >= 10:
                code_snippet_min_10_lines.append(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "\n")
    write_lines(code_snippet_min_10_lines, output)


def write_lines(contents, path):
    file_writer = open(path, 'w')
    file_writer.writelines(contents)
    file_writer.close()


if __name__ == "__main__":
    code_snippet_csv = "/home/mrhmisu/Downloads/js_accepted_code_snippet.csv"
    code_snippet_min_10_lines = "/home/mrhmisu/Downloads/js_accepted_code_snippet_min10Lines.csv"
    filter_code_snippet_by_loc(code_snippet_csv, code_snippet_min_10_lines);
    sys.exit()
