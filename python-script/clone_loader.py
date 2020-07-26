import csv


# /home/mrhmisu/UCL-MS/Test-Data/query/clone-detector/type-2-detector.js_getClonePairsWithoutIndexMaking#9#28,/home/mrhmisu/UCL-MS/Test-Data/index/clone-detector/type-2-detector.js_getClonePairsWithoutIndexMaking#9#28


def load_clone_pair_from_csv_report(path):
    pairs = [];
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            element_one = row[0].split("#")
            element_two = row[1].split("#")
            clone_pair = get_clone_pair(element_one, element_two);
            pairs.append(clone_pair)
        return pairs


def get_clone_pair(element_one, element_two):
    clone_pair = {}
    path_one = element_one[0].split(".js_")[0] + ".js"
    path_two = element_two[0].split(".js_")[0] + ".js"
    code_one = get_source_Code(path_one, int(element_one[1]), int(element_one[2]))
    code_two = get_source_Code(path_two, int(element_two[1]), int(element_two[2]))
    clone_pair["c1"] = code_one;
    clone_pair["c2"] = code_two;
    return clone_pair;


def get_source_Code(filePath, start, end):
    with open(filePath) as f:
        lines = f.readlines()
    codes_lines = lines[(start - 1):(end - 1)];
    code = '\n'.join(codes_lines)
    return code;


if __name__ == "__main__":
    clone_report_path = "/home/mrhmisu/UCL-MS/Test-Data/test_qr_06-07-20_13-33-811.csv"
    clones = load_clone_pair_from_csv_report(clone_report_path)
    for clone in clones:
        print("xxxxxxxxxxxxxxxxxxxxxxx Pair Start xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(clone["c1"])
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxXXXXXXXXXXXX")
        print(clone["c2"])
        print("xxxxxxxxxxxxxxxxxxxxxxxxPair End xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
