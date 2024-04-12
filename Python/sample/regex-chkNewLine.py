# check any line have char ;:。 in middle
import re

def check_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()  # Trim leading and trailing whitespace
            if re.search(r'[;:。](?![_）（"])(?=[^\n])', line):
            # if re.search(r'[;:。](?=[^\n])', line): #without filter
                print(f"Line {line_number}: {line.strip()}")

# Replace 'filename.txt' with the name of your file
check_lines( 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014.txt')