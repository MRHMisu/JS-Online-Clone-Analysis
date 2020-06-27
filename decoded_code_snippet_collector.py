"""

Decode and collect code snippet from the SO extracted code snippet csv.

"""

import csv
import sys


def decode_code_snippet_from_csv(path):
    frequency_map = {}
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            answer_id = row[0]
            question_id = row[1]
            loc = row[2]
            code_snippet = bytes.fromhex(row[3]).decode('utf-8')
            print(code_snippet)
            print("\n-------------------------\n")
        return frequency_map


if __name__ == "__main__":
    code_snippet_csv = sys.argv[1]
    # decoded_code_snippet_output = sys.argv[2]
    decode_code_snippet_from_csv(code_snippet_csv)
    sys.exit()
