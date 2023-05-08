from util.types import HTree


def load_file(filename: str) -> str:
  try:
    content = open(filename).read()
  except Exception as e:
    print("could not load filname, error:", e, sep="\n")
    exit(1)
  return content


def padding(num: str) -> str:
  while len(num) != 8:
    num = "0" + num
  return num


def dump_to_file(encoded_message: str, filename: str):
  encoded_bytes = int(encoded_message, 2).to_bytes(
      (len(encoded_message) + 7) // 8, byteorder='big')

  with open(filename, "wb") as f:
    f.write(encoded_bytes)

  with open(filename, "rb") as f:
    back_bytes = f.read()

  back = "".join([bin(byte)[2:].zfill(8) for byte in back_bytes])
  print("got:", back)


def compress_file(filename: str):
  content = load_file(filename)
  bin_content = "".join([padding(bin(ord(char))[2:]) for char in content])

  ht = HTree(content)
  print("send:", ht.encoded_content)

  # TODO: check if the binary representation of the content is correct and makes sense to compare this way
  ratio = len(ht.encoded_content) / len(bin_content)
  print("ratio:", ratio)

  output_file = filename + ".hc"
  # dump_to_file(ht, output_file)
