"""
Export data in proNet-core's input data format:
    eg:
        <source.data>                  ->             <export.datat>
        user   itemList                               user item  weight
        u1     item1 item2 item3 ...                  u1   item1 1
                                                      u1   item2 1
                                                      u1   item3 1
                                                      ...
"""

import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument("file",
                    type=str,
                    help="Relative path of file which is to be converted.")
PARSER.add_argument("-o",
                    "--output",
                    default='../data/proNet_input.data',
                    type=str,
                    help="Output path of converted file. (default: export.data)")
ARGS = PARSER.parse_args()
FILEPATH = ARGS.file
OUTPUT = ARGS.output
with open(OUTPUT, 'wt') as fout:
    with open(FILEPATH, 'rt') as fin:
        for line in fin:
            user, *items = line.strip().split(' ')
            for item in items:
                fout.write(f"u{user} {item} 1\n")
