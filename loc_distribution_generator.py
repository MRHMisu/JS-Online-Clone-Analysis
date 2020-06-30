"""
Generate a LOC (Line Of Code) distribution based SO extracted code snippets
"""

import csv
import sys

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



def group_code_snippet_by_loc(path, output):
    lines=[];
    lines.append("group,loc\n");
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            loc = int(row[2])
            if loc <6:
                group= "Boiler-Plate"
            elif loc < 10:
                group = "Fair"
            elif loc >= 10:
                group = "Good"
            element=str(group)+","+str(loc)+"\n"
            lines.append(element)
    write_lines(lines, output)

def write_lines(contents, path):
    file_writer = open(path, 'w')
    file_writer.writelines(contents)
    file_writer.close()

def extract_loc_frequency_of_code_snippet(path):
    frequency_map = {}
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            loc = int(row[2])
            if loc in frequency_map:
                frequency_map[loc] = frequency_map[loc] + 1
            else:
                frequency_map[loc] = 1
    frequency_map = dict(sorted(frequency_map.items()))
    print(frequency_map)
    return frequency_map



def get_loc(path):
    lines = []
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            loc = int(row[2])
            lines.append(loc)
    lines = list(filter((1).__ne__, lines))
    lines = list(filter((2).__ne__, lines))
    lines = list(filter((3).__ne__, lines))
    return np.array(lines)






if __name__ == "__main__":
    # code_snippet_csv = sys.argv[1]
    # loc_distribution_output = sys.argv[2]
    code_snippet_csv = "/home/stackoverflow/java_accepted_code_snippet.csv"
    code_snippet_catagory="/home/stackoverflow/java_code_snippet_catagory.csv"
    group_code_snippet_by_loc(code_snippet_csv,code_snippet_catagory)
    #extract_loc_frequency_of_code_snippet(code_snippet_csv)
    #code_snippet_loc = get_loc(code_snippet_csv)
    #max_line=max(code_snippet_loc)
    #min_line=min(code_snippet_loc);

    #print("max="+str(max_line));
    #print("min=" + str(min_line));

    sys.exit()
