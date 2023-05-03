#!/usr/bin/env python3

import sys
from dataclasses import dataclass

from huff import compress_file

@dataclass(frozen=True)
class HFile:
  translation_dictionary: dict[str, str]
  encoded_message: str


def dump_to_file(encoded_message: str, filename: str):
  encoded_bytes = int(encoded_message, 2).to_bytes((len(encoded_message) + 7) // 8, byteorder='big')

  with open("output.bin", "wb") as f:
    f.write(encoded_bytes)

  with open("output.bin", "rb") as f:
    back_bytes = f.read()

  back = "".join([bin(byte)[2:].zfill(8) for byte in back_bytes])
  print("got:", back)


if __name__ == "__main__":
  # TODO: maybe add proper command line arguments (i.e -o, --output, -h, --help)?
  if len(sys.argv) < 1:
    print("no file given")
    exit(1)

  filename = sys.argv[1]
  translation_dictionary, encoded_message = compress_file(filename)