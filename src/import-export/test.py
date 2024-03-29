import itertools

file_to_save = 'pair-length-ratio.py'
start = "7"
end = "40"


def read_line_with_range(file_path, star, end):
    lines = []
    with open(file_path, "r") as text_file:
        for line in itertools.islice(text_file, star, end):
            lines.append(line)
    return '\n'.join(lines)


code = read_line_with_range(file_to_save, int(start) - 1, int(end))
print(code)
