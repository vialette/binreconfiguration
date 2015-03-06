"""Storage unit snapshot"""

class Snapshot(object):

  def __init__(self, storage_unit):
    self._bin_snapshots  = [bin.snapshot() for bin in storage_unit]
    self._number_of_bins = len(storage_unit)

  def __len__(self):
    """Return the number of bins in this storage unit snapshot."""
    return self._number_of_bins

  def __str__(self):
    """Stringify this storage unit snapshot."""
    return '(' + ','.join([str(bin_snapshot) for bin_snapshot in self]) + ')'

  def __getitem__(self, i):
    """Access """
    return self._bin_snapshots[i]

  def __iter__(self):
    """Iterate over all bin snapshots."""
    return iter(self._bin_snapshots)

  def first(self):
    """Return the snapshot of the first bin."""
    return self[0]

  def last(self):
    """Return the snapshot of the last bin."""
    return self[-1]
