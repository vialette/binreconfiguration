from .snapshot import Snapshot
from .storageunit import StorageUnit
from .storageunitexception import StorageUnitException

class UniformStorageUnit(StorageUnit):

	def __init__(self, bins = None, snapshots = None, name = None):
		super(UniformStorageUnit, self).__init__(bins, snapshots, name)
		if len(self._bins) > 0:
			capacities = [bin.capacity() for bin in self._bins]
			if not capacities.count(capacities[0]) == len(capacities):
				raise StorageUnitException("bins have different capacities")


