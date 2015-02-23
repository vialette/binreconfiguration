from .storageunit import StorageUnit

class SnapshotedStorageUnit(StorageUnit):

	def __init__(self, name = None):
		super(SnapshotedStorageUnit, self).__init__(name)
		self._snapshots = []

	def add_item(self, index, item):
		super(SnapshotedStorageUnit, self).add_item(index, item)
		self._snapshots.append(self.snapshot())

	def snapshots(self):
		return self._snapshots