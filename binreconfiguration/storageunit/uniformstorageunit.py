from .snapshot import Snapshot
from storageunitexception import StorageUnitException

class UniformStorageUnit(StorageUnit):

	def __init__(self, bins = None, snapshot_controller = None, name = None):
		super(UniformStorageUnit, self).__init__(bins, snapshot_controller, name)
		if len(self._bins) > 0:
			capacities = [bin.capacity() for bin in self._bins]
			if not capacities.count(capacities[0]) == len(capacities):
				raise StorageUnitException("bins have different capacities")


