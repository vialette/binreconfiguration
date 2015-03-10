"""Storage unit snapshot

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

class Snapshot(object):

  def __init__(self, storage_unit):
    self._bin_snapshots  = [bin.snapshot() for bin in storage_unit]
    self._number_of_bins = len(storage_unit)

  def __len__(self):
    """Return the number of bins in this storage unit snapshot.
    """
    return self._number_of_bins

  def __str__(self):
    """Stringify this storage unit snapshot.
    """
    return '(' + ','.join([str(bin_snapshot) for bin_snapshot in self]) + ')'

  def __getitem__(self, i):
    """Access the bin snapshot of a given bin index.
    """
    return self._bin_snapshots[i]

  def bin_snapshot_by_index(self, bin_index):
    """Return the bin snapshot of a given bin index.

    """
    return self[i]

  def bin_snapshot_by_name(self, bin_name):
    """Return the bin snapshot of a given bin name."""
    return next(bin_snapshot for bin_snapshot in self._bin_snapshots if bin_snapshot.bin_name() == bin_name)

  def __iter__(self):
    """Iterate over all bin snapshots of this storage unit snapshot.
    """
    return iter(self._bin_snapshots)
