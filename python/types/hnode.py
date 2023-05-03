class HNode:

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