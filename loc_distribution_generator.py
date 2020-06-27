"""
Generate a LOC (Line Of Code) distribution based SO extracted code snippets
"""

import csv
import sys

import matplotlib.pyplot as plt
import numpy as np


def extract_loc_frequency_of_code_snippet(path):
    frequency_map = {}
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            loc = row[2]
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
    return np.array(lines)


if __name__ == "__main__":
    # code_snippet_csv = sys.argv[1]
    # loc_distribution_output = sys.argv[2]
    code_snippet_csv = "sample_snippet_output.csv"
    extract_loc_frequency_of_code_snippet(code_snippet_csv)
    code_snippet_loc = get_loc(code_snippet_csv)

    # matplotlib histogram
    plt.hist(code_snippet_loc, color='blue', edgecolor='black',
             bins=int(180 / 5))

    # seaborn histogram
    # sns.distplot(code_snippet_loc, hist=True, kde=False, bins=32, color='blue',
    #           hist_kws={'edgecolor': 'black'})

    # Add labels
    plt.title('LOC Distribution in SO Code Snippets')
    plt.xlabel('LOC')
    plt.ylabel('Frequency')
    # plt.ylim(0, 50)
    # plt.xlim(0, 50)
    plt.xticks(list(range(0, 90,5))) 

    # fig = plt.gcf()
    plt.show()
    # plt.draw()
    # fig.savefig('loc_distribution.png', dpi=100)
    sys.exit()
