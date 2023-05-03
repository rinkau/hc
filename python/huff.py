
from collections import Counter
from heapq import heappush as push
from heapq import heappop as pop


translation = {} 

def load_file(filename: str) -> tuple[str, dict[str, int]]:
  try:
    content = open(filename).read()
  except Exception as e:
    print("could not load filname, error:", e, sep="\n")
    exit(1)

  return content, Counter(content)


class Node:

  def __init__(self, char, count, lo=None, hi=None, encoding=""):
    self.char = char
    self.count = count
    self.lo = lo
    self.hi = hi
    self.encoding = encoding

  def __lt__(self, other):
    return self.count < other.count

  def __str__(self) -> str:
    return f"{ord(self.char)}: {self.count}"


def build_priority_queue(counter: dict[str, int]) -> list[Node]:
  heap: list[Node] = []
  for char, ocurrency in counter.items():
    push(heap, Node(char, ocurrency))
  return heap


def build_tree(heap: list[Node]) -> Node:
  while len(heap) > 1:
    lo = pop(heap)
    hi = pop(heap)
    push(heap, Node("", lo.count + hi.count, lo, hi))
  return pop(heap)


def encode_tree(root: Node):
  global translation
  if root.lo == None:  # root is a leaf
    translation[root.char] = root.encoding
    return

  root.lo.encoding = root.encoding + "0"
  root.hi.encoding = root.encoding + "1"

  encode_tree(root.lo)
  encode_tree(root.hi)


def encode(content: str) -> str:
  return "".join([translation[char] for char in content])


def padding(num: str) -> str:
  while len(num) != 8:
    num = "0" + num
  return num


def compress_file(filename: str):
  global translation

  content, counter = load_file(filename)
  pq = build_priority_queue(counter)
  root = build_tree(pq)
  encode_tree(root)

  bin_content = "".join([padding(bin(ord(char))[2:]) for char in content])
  encoded_message = encode(content)
  print("send:", encoded_message)

  ratio = len(encoded_message) / len(bin_content)
  print("ratio:", ratio)
  return translation, encoded_message


