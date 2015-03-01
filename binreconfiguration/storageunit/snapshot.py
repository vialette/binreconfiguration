"""Storage unit snapshot"""

class Snapshot(object):

  def __init__(self, storage_unit):
    self._bin_snapshots  = [bin.snapshot() for bin in storage_unit]
    self._number_of_bins = len(storage_unit)

  def __len__(self):
    return self._number_of_bins

  def __str__(self):
    return '(' + ','.join([str(bin_snapshot) for bin_snapshot in self]) + ')'

  def __getitem__(self, i):
    return self._bin_snapshots[i]

  def __iter__(self):
    return iter(self._bin_snapshots)

  def first(self):
    return self[0]

  def last(self):
    return self[-1]
