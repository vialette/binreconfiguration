"""Dynamic storage unit

"""

from .storageunit import StorageUnit
from .snapshot import Snapshot

class DynamicStorageUnit(StorageUnit):

	def add_bins(self, bins):
		for bin in bins:
			self.add_bin(bin)

	def add_bin(self, bin):
		self._bins.append(bin)

	def remove_bins(self, bins):
		for bin in bins:
			self.remove_bin(bin)

	def remove_bin(self, bin):
		self._bins.remove(bin)
