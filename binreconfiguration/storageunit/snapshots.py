"""Storage unit snapshots"""

class Snapshots(object):
 
  def __init__(self):
    self._storage_unit_snapshots = []

  def append(self, storage_unit_snapshot):
    self._storage_unit_snapshots.append(storage_unit_snapshot)

  def add(self, snapshot):
    self._storage_unit_snapshots.append(snapshot)

  def __getitem__(self, index):
    return self._storage_unit_snapshots[index]

  def __iter__(self):
    return iter(self._storage_unit_snapshots)

  def __len__(self):
    return len(self._storage_unit_snapshots)

  def last(self):
    return self._storage_unit_snapshots[-1]





