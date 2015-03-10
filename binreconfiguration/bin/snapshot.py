"""Bin snapshot"""

class Snapshot(object):

  def __init__(self, bin):
    pairs = [(key, bin[key]) for key in sorted(dir(bin))]
    self._dict = dict(pairs)
    self._dict['name'] = bin.name()

  def __str__(self):
    return "(" + ",".join(["{}={}".format(key, self._dict[key]) for key in sorted(self._dict)]) + ")"

  def __getitem__(self, key):
    return self._dict[key.lower()]

  def __iter__(self):
    return iter(self._dict)

  def bin_name(self):
    return self._dict['name']