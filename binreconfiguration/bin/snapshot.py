"""Bin snapshot"""

class Snapshot(object):

  COUNT = "count"
  SIZE  = "size"

  def __init__(self, count, size):
    self._dict([(COUNT, count), (SIZE, size)])

  def __str__(self):
    return "(count={}, size={})".format(self._count, self._size)

  __repr__ = __str__

  def count(self):
    return self._dict[COUNT]

  def size(self):
    return self._dict[SIZE]

  def __getitem__(self, key):
    return self._dict[key.lower()]