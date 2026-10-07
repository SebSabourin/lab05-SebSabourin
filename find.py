# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    # TODO: add an optional flag -i / --ignore-case  (use action="store_true")
    parser.add_argument("-i", "--ignore-case", action ="store_true", help = "match without looking for upper/lower cases")

    args = parser.parse_args()

    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).
    file = parser.parse_args()

    file = open(args.filename)
    lines = file.readlines()
    file.close

    line_number = 1
    for line in lines:
        line = line.rstrip("\n")

        if args.ignore_case:
            if args.pattern.lower() in line.lower():
                print(str(line_number) + ": " + line)
        else:
            if args.pattern in line:
                print(str(line_number) + ": " + line)

        line_number = line_number + 1

if __name__ == "__main__":
    main()
