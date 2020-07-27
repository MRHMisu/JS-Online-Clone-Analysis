import csv
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_distribution(code_snippet_catagory_path):
    df = pd.read_csv(code_snippet_catagory_path)
    df.head()
    x1 = df.loc[df.group == "Boiler-Plate", "loc"]
    x2 = df.loc[df.group == "Fair", "loc"]
    x3 = df.loc[df.group == "Good", "loc"]

    sns.set_style("white")

    # Plot
    kwargs = dict(hist_kws={'alpha': .6}, kde_kws={'linewidth': 2})

    plt.figure(figsize=(10, 7), dpi=80)
    sns.distplot(x1, color="dodgerblue", label="Compact", **kwargs)
    sns.distplot(x2, color="orange", label="SUV", **kwargs)
    sns.distplot(x3, color="deeppink", label="minivan", **kwargs)

    plt.gca().set(title='Frequency Histogram of Code Snippets', ylabel='Frequency')
    plt.xlim(0, 1340)
    plt.xticks(list(range(0, 1340, 20)))
    plt.legend()
    plt.show()


def extract_loc_catagory(path):
    frequency_map = {}
    frequency_map["Boiler-Plate"] = 0;
    frequency_map["Fair"] = 0;
    frequency_map["Good"] = 0;

    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            if row[0] == "Boiler-Plate":
                frequency_map["Boiler-Plate"] = frequency_map["Boiler-Plate"] + 1;
            elif row[0] == "Fair":
                frequency_map["Fair"] = frequency_map["Fair"] + 1;
            elif row[0] == "Good":
                frequency_map["Good"] = frequency_map["Good"] + 1;
    print(frequency_map)
    return frequency_map


def extract_loc_frequency_of_code_snippet(path):
    frequency_map = {}
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            loc = int(row[1])
            if loc in frequency_map:
                frequency_map[loc] = frequency_map[loc] + 1
            else:
                frequency_map[loc] = 1
    frequency_map = dict(sorted(frequency_map.items()))
    print(frequency_map)
    return frequency_map


if __name__ == "__main__":
    # code_snippet_csv = sys.argv[1]
    # loc_distribution_output = sys.argv[2]
    python_code_snippet_catagory = "python_code_snippet_catagory.csv"
    js_code_snippet_catagory = "js_code_snippet_catagory.csv"
    java_code_snippet_catagory = "java_code_snippet_catagory.csv"
    # generate_distribution(code_snippet_catagory)
    #extract_loc_catagory(java_code_snippet_catagory)
    #extract_loc_catagory(python_code_snippet_catagory)
    #extract_loc_catagory(js_code_snippet_catagory)


    sys.exit()
