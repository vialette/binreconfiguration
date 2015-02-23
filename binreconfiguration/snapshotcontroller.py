class SnapshotController(object):
  def __init__(self, storage_unit):
    self._storage_unit = storage_unit
    self._storage_unit_snapshots = []

  def storage_unit(self):
    return self._storage_unit

  def append(self, storage_unit_snapshot):
    self._storage_unit_snapshots.append(storage_unit_snapshot)

  def __getitem__(self, index):
    return self._storage_unit_snapshots[index]

  def __iter__(self):
    return iter(self._storage_unit_snapshots)

  def __len__(self):
    return len(self._storage_unit_snapshots)