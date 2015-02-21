from .storageunit import StorageUnit

class SnapshotedStorageUnit(StorageUnit):

	def __init__(self, name):
		super(SnapshotedStorageUnit, self).__init__(name)
		self._snapshots = []

	def add_item(self, item):
		super(SnapshotedStorageUnit, self).add_item(item)
		self._snapshots.append(self.snapshot())

	def snapshots(self):
		return self._snapshots