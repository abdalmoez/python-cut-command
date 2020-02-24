#!/usr/bin/env python
import argparse
import sys

def process_line(indexes , line, delimiter):
    words = line.split(delimiter)
    l = len(words)
    ch = ""
    for i in indexes:
        if( i - 1 < l ):
            ch += words[i - 1] + " "
    print(ch)

delimiter = '\t'
parser = argparse.ArgumentParser(description='Cut text')
parser.add_argument('-f', '--filter', type=str, help='list of columns index starting from 1')
parser.add_argument('-d', '--delimiter', nargs='?', type=str, help='delimiter')
parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'))

args = parser.parse_args()
columns = [int(numeric_string) for numeric_string in args.filter.split(',')]
if(args.delimiter != None):
    delimiter = args.delimiter
if(args.input_file != None):
    for line in args.input_file:
        process_line(columns, line.strip(), delimiter)
else:
    try:
        for line in sys.stdin:
            process_line(columns, line.strip(), delimiter)
    except KeyboardInterrupt:
        sys.stdout.flush()
        pass
