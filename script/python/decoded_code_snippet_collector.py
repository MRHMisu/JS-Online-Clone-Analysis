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
    #code_snippet_csv = sys.argv[1]
    # decoded_code_snippet_output = sys.argv[2]
    #decode_code_snippet_from_csv(code_snippet_csv)
    print(bytes.fromhex("3c612069643d226153686f774869646522206f6e636c69636b3d27546f67676c65446973706c617928262333393b3c2523204461746142696e6465722e4576616c28436f6e7461696e65722e446174614974656d2c20224a6f62436f6465222920253e262333393b293b273e53686f772f486964653c2f613e0a").decode('utf-8'))
    sys.exit()
