#!/usr/bin/env python3

import argparse
import os

from huff import compress_file


def main():
  # TODO: add a loading bar and a step by step log along with it

  parser = argparse.ArgumentParser(description="HC command line tool")
  parser.add_argument("-c",
                      "--create",
                      action="store_true",
                      help="Compress a text file")

  parser.add_argument("-x",
                      "--extract",
                      action="store_true",
                      help="Extract .hc file")
  parser.add_argument("filename",
                      type=str,
                      help="Name of the file to operate on")
  args = parser.parse_args()

  if args.create:
    if os.path.isfile(args.filename):
      print(f"Compressing {args.filename}...")
      compress_file(args.filename)
    else:
      print(f"{args.filename} does not exist or is not a file")
  elif args.extract:
    if os.path.isfile(args.filename):
      # TODO:
      print(f"Extracting from {args.filename}...")
    else:
      print(f"{args.filename} does not exist or is not a file")
  else:
    parser.print_help()


if __name__ == "__main__":
  main()
