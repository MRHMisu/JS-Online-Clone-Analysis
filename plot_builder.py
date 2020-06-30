
import csv
import sys

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def generate_distribution(code_snippet_catagory_path):
    df = pd.read_csv(code_snippet_catagory_path)
    df.head()
    x1 = df.loc[df.group == "Boiler-Plate", "loc"]
    x2 = df.loc[df.group == "Fair", "loc"]
    x3 = df.loc[df.group == "Good", "loc"]

    kwargs = dict(alpha=0.5, bins=100)

    plt.hist(x1, **kwargs, color='g', label='Boiler-Plate')
    plt.hist(x2, **kwargs, color='b', label='Fair')
    plt.hist(x3, **kwargs, color='r', label='Good')
    plt.gca().set(title='Frequency Histogram of Code Snippets', ylabel='Frequency')
    plt.xlim(0, 1340)
    plt.xticks(list(range(0, 1340, 5)))
    plt.legend();
    plt.show();


if __name__ == "__main__":
    # code_snippet_csv = sys.argv[1]
    # loc_distribution_output = sys.argv[2]
    code_snippet_catagory="/home/stackoverflow/python_code_snippet_catagory.csv"
    generate_distribution(code_snippet_catagory)
    sys.exit()