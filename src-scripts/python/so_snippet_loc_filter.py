import csv
import sys


def filter_code_snippet_by_loc(so_snippet_path, output, loc):
    filtered_snippet_path = []
    header = "question_id" + "," + "answer_id" + "," + "block_position" + "," + "loc" + "," + "code_snippet" + '\n'
    filtered_snippet_path.append(header)
    with open(so_snippet_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)# skip the header
        for row in readCSV:
            line_of_code = int(row[3])
            if line_of_code >= loc:
                filtered_snippet_path.append(row[0] + "," + row[1] + "," + row[2] + "," + row[3]+ "," + row[4]+"\n")
    write_lines(filtered_snippet_path, output)


def write_lines(contents, path):
    file_writer = open(path, 'w')
    file_writer.writelines(contents)
    file_writer.close()


if __name__ == "__main__":
    code_snippet_csv = sys.argv[1]
    outputPath = sys.argv[2]
    loc=sys.argv[3]
    filter_code_snippet_by_loc(code_snippet_csv, outputPath, loc)
    sys.exit()
