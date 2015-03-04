"""Overflow simulator"""

from binreconfiguration.bin import Bin
from binreconfiguration.storageunit import UniformStorageUnit
from binreconfiguration.storageunit import Snapshots
from binreconfiguration.overflowexception import OverflowException

class Overflow(object):

	def __init__(self, number_of_bins, capacity):
		self._number_of_bins = number_of_bins
		self._capacity       = capacity

	def run(self, strategy_factory, items):
		# construct bins
		bins = [Bin(self._capacity) for _ in range(self._number_of_bins)]

		# 
		storage_unit = UniformStorageUnit(bins = bins, snapshots = Snapshots())

		#
		strategy = strategy_factory(storage_unit)

		# add items
		for item in items():
			try:
				strategy.add_item(item)
			except OverflowException:
				return storage_unit.snapshots()
