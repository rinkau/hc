#!/usr/bin/env python3

import sys

from huff import compress_file

if __name__ == "__main__":
  # TODO: maybe add proper command line arguments (i.e -o, --output, -h, --help)?
  if len(sys.argv) < 1:
    print("no file given")
    exit(1)

  filename = sys.argv[1]
  compress_file(filename)