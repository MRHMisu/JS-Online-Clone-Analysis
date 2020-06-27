"""
Generate a LOC (Line Of Code) distribution based SO extracted code snippets
"""


import csv
import sys


def extract_loc_frequency_of_code_snippet(path):
    frequency_map = {}
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            loc = row[2]
            if loc in frequency_map:
                frequency_map[loc] = frequency_map[loc]  + 1
            else:
                frequency_map[loc] = 1
    print(frequency_map)
    return frequency_map


# def frequency_distribution_plotter(frequency_map):


if __name__ == "__main__":
    code_snippet_csv = sys.argv[1]
    # loc_distribution_output = sys.argv[2]
    extract_loc_frequency_of_code_snippet(code_snippet_csv);
    sys.exit()
