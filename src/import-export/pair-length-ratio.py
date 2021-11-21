import csv

so_snippet_base_path = '/home/ubuntu/experiment/so-query/'
github_snippet_base_path = '/home/ubuntu/experiment/git-js-corpus/'


def calculate_length_ratio(clone_report, length_ratio_path):
    all_pairs_line = []
    serial_no = 0
    with open(clone_report) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            serial_no += 1
            clone_method1, start1, end1 = row[0].split('#')
            clone_method1 = clone_method1.split(".js_")[0] + ".js"
            clone_method1 = clone_method1[len(so_snippet_base_path):]
            so_snippet_length = (int(end1) - int(start1)) + 1

            for i in range(1, len(row)):
                git_snippet_rank = i
                clone_method2, start2, end2 = row[i].split('#')
                clone_method2 = clone_method2.split(".js_")[0] + ".js"
                clone_method2 = clone_method2[len(github_snippet_base_path):]
                git_snippet_length = (int(end2) - int(start2)) + 1
                length_ratio = float((so_snippet_length / git_snippet_length))

                # if length_ratio >= 0.5:
                pair = str(serial_no) + "," + str(
                    git_snippet_rank) + "," + clone_method1 + "," + start1 + "," + end1 + "," + str(
                    so_snippet_length) + "," + clone_method2 + "," + start2 + "," + end2 + "," + str(
                    git_snippet_length) + "," + str(
                    length_ratio) + '\n'
                all_pairs_line.append(pair)
                # put break to consider only the 1st rank that's length ratio >=0.5
                # break

        write_lines(all_pairs_line, length_ratio_path)


def write_lines(contents, path):
    file_writer = open(path, 'w')
    file_writer.writelines(contents)
    file_writer.close()


def execute_script():
    clone_report_path = "test_qr_12-08-20_09-52-406.csv"
    # length_ratio_path = "unique_top_rank pairs_len_ratio_0.5.csv"
    # length_ratio_path = "pair-data/all_pairs_length_ratio_0.5_greater.csv"
    length_ratio_path = "pair-data/all_pairs.csv"
    calculate_length_ratio(clone_report_path, length_ratio_path)


execute_script()
