#!/usr/bin/env python3

import argparse
import os

from typing import Callable

from compressor import compress_file


def validate(filename: str, error_message: str):
  if os.path.isfile(filename):
    return

  print(error_message)
  exit(1)


def run_pipeline(filename: str, handler: Callable[[str], None],
                 error_message: str):
  validate(filename, error_message)
  handler(filename)


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
    run_pipeline(args.filename, compress_file,
                 f"{args.filename} doesn't exist or isn't a file")

  elif args.extract:
    run_pipeline(args.filename,
                 lambda x: print(f"Extracting from {args.filename} ..."),
                 f"{args.filename} doesn't exist or isn't a file")

  else:
    parser.print_help()


if __name__ == "__main__":
  main()
