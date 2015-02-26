import abc

class BaseSnapshot(metaclass = abc.ABCMeta):

  def __init__(self, bin, keys = 'ALL'):
    if keys == 'ALL' or keys == '*':
      keys = bin.keys()
    pairs = [(key, bin[key]) for key in sorted(bin.keys()) if key in keys]
    self._dict = dict(pairs)

  def __str__(self):
    return "(" + ",".join(["{}={}".format(key, self._dict[key]) for key in sorted(self._dict)]) + ")"

  def count(self):
    return self._dict[self.COUNT]

  def size(self):
    return self._dict[self.SIZE]

  def __getitem__(self, key):
    return self._dict[key.lower()]

  def __iter__(self):
    return iter(self._dict)