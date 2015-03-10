"""Bin snapshot.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

class Snapshot(object):

  def __init__(self, bin):
    pairs = [(key, bin[key]) for key in sorted(dir(bin))]
    self._dict = dict(pairs)
    self._dict['name'] = bin.name()

  def __str__(self):
    """Stringify this bin snapshot.
    """
    return "(" + ",".join(["{}={}".format(key, self._dict[key]) for key in sorted(self._dict)]) + ")"

  def __getitem__(self, key):
    """Return the value of a given key in this bin snapshot.


    :param key: The key.
    :type key: string.
    """
    return self._dict[key.lower()]

  def __iter__(self):
    """Iterate over all keys of this bin snapshot.
    """
    return iter(self._dict)

  def bin_name(self):
    """Return the name of the bin of this bin storage unit.
    """
    return self._dict['name']