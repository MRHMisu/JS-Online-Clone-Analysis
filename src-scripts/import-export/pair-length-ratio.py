import csv


def calculate_length_ratio(clone_report, length_ratio_path):
    lines = []
    serial_no = 0
    with open(clone_report) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            serial_no += 1
            clone_method1, start1, end1 = row[0].split('#')
            so_snippet_length = (int(end1) - int(start1))

            for i in range(1, len(row)):
                git_snippet_rank = i
                clone_method2, start2, end2 = row[i].split('#')
                git_snippet_length = (int(end2) - int(start2))
                length_ratio = float((so_snippet_length / git_snippet_length))
                pair = str(serial_no) + "," + row[0] + "," + row[i] + "," + str(git_snippet_rank) + "," + str(
                    length_ratio) + '\n'
                lines.append(pair)
        write_lines(lines, length_ratio_path)


def write_lines(contents, path):
    file_writer = open(path, 'w')
    file_writer.writelines(contents)
    file_writer.close()


def execute_script():
    clone_report_path = "test_qr_12-08-20_09-52-406.csv"
    length_ratio_path = "test_qr_12-08-20_09-52-406-all-pairs.csv"
    calculate_length_ratio(clone_report_path, length_ratio_path)


execute_script()
