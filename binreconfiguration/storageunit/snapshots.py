"""Storage unit snapshots"""

class Snapshots(object):
 
  def __init__(self):
    self._storage_unit_snapshots = []

  def append(self, storage_unit_snapshot):
    """Append a storage unit snapshot to the snapshot list."""
    self._storage_unit_snapshots.append(storage_unit_snapshot)

  def add(self, snapshot):
    """Add a storage unit snapshot to the snapshot list.

    See *append*.
    """
    self._storage_unit_snapshots.append(snapshot)

  def __getitem__(self, index):
    """Return a storage unit snapshot."""
    return self._storage_unit_snapshots[index]

  def __iter__(self):
    """Iterate over all sotorage unit snapshots."""
    return iter(self._storage_unit_snapshots)

  def __len__(self):
    """Return the number of storage unit snapshots."""
    return len(self._storage_unit_snapshots)

  def last(self):
    """Return the last storage unit snapshot."""
    return self._storage_unit_snapshots[-1]





