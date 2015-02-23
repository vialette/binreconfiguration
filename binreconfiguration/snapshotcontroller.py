class SnapshotController(object):
  def __init__(self):
    self._snapshots    = []

  def storage_unit(self):
    return self._storage_unit

  def append(self, snapshot):
    self._snapshots.append(snapshot)

  def __getitem__(self, index):
    return self._snapshots[index]

  def __iter__(self):
    return iter(self._snapshots)

  def __len__(self):
    return len(self._snapshots)

  def projection(self, keys):
    return [self._projection(snapshot, keys) for snapshot in self._snapshots]

  def _projection(self, snapshot, keys):
    return dict([(key, snapshot[key]) for key in snapshot if key in keys])




