from .dynamicstorageunit import DynamicStorageUnit
from .snapshot import Snapshot

class DynamicUniformStorageUnit(DynamicStorageUnit):

	def __init__(self, bins = None, snapshot_controller = None, name = None):
		super(UniformStorageUnit, self).__init__(bins, snapshot_controller, name)
		if len(self._bins) > 0:
			capacities = [bin.capacity() for bin in self._bins]
			if not capacities.count(capacities[0]) == len(capacities):
				raise StorageUnitException("bins have different capacities")
			self._capacity = capacities[0]
		else:
			self._capacity = None

	def add_bin(self, bin):
		if self._capacity is not None:
			if bin.capacity() != self._capacity:
				raise StorageUnitException("bins have different capacities")
		
		self._capacity = bin.capacity()
		super(DynamicUniformStorageUnit, self).add_bin(bin)