"""Overflow simulator"""

from binreconfiguration.bin import Bin
from binreconfiguration.storageunit import UniformStorageUnit
from binreconfiguration.storageunit import Snapshots
from binreconfiguration.overflowexception import OverflowException

class Overflow(object):

	def __init__(self, number_of_bins, capacity):
		self._number_of_bins = number_of_bins
		self._capacity       = capacity

	def run(self, strategy_factory, generator):
		# construct the bins
		bins = [Bin(self._capacity, "bin-{}.".format(i)) for i in range(self._number_of_bins)]

		# construct the (uniform) storage unit
		storage_unit = UniformStorageUnit(bins = bins, snapshots = Snapshots())

		# 
		strategy = strategy_factory(storage_unit)

		# add items
		for item in generator:
			try:
				strategy.add_item(item)
			except OverflowException:
				return storage_unit.snapshots()
