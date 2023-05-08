from heapq import heappush as push
from heapq import heappop as pop
from collections import Counter


class HNode:

  def __init__(self, char, count, lo=None, hi=None, encoding=""):
    self.char = char
    self.count = count
    self.lo = lo
    self.hi = hi
    self.encoding = encoding

  def __lt__(self, other) -> bool:
    return self.count < other.count

  def __str__(self) -> str:
    return f"{ord(self.char)}: {self.count}"


class HTree:

  def __init__(self, content: str):
    self.content = content
    self.translation: dict[str, str] = {}
    self.root = self.build_tree()
    self.encode_tree(self.root)
    self.encoded_content = self.encode_content()

  def build_tree(self):
    character_frequency = Counter(self.content)
    pq = self.enqueue_counter(character_frequency)
    return self.extract_tree(pq)

  def extract_tree(self, heap: list[HNode]) -> HNode:
    while len(heap) > 1:
      lo = pop(heap)
      hi = pop(heap)
      push(heap, HNode("", lo.count + hi.count, lo, hi))
    return pop(heap)

  def enqueue_counter(self, character_frequency: Counter) -> list[HNode]:
    heap: list[HNode] = []
    for char, ocurrency in character_frequency.items():
      push(heap, HNode(char, ocurrency))
    return heap

  def encode_tree(self, root: HNode):
    if root.lo == None:  # root is a leaf
      self.translation[root.char] = root.encoding
      return

    root.lo.encoding = root.encoding + "0"
    root.hi.encoding = root.encoding + "1"

    self.encode_tree(root.lo)
    self.encode_tree(root.hi)

  def encode_content(self) -> str:
    return "".join([self.translation[char] for char in self.content])
