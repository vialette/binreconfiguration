"""Bin snapshot"""

class Snapshot(object):

  def __init__(self, count, size):
    self._count = count
    self._size  = size

  def __str__(self):
    return "(count={}, size={})".format(self._count, self._size)

  __repr__ = __str__

  def count(self):
    return self._count

  def size(self):
    return self._size