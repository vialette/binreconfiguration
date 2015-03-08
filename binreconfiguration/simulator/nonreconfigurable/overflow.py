"""Overflow simulator"""

from binreconfiguration.simulator import Simulator
from binreconfiguration.bin import Bin
from binreconfiguration.storageunit import UniformStorageUnit
from binreconfiguration.storageunit import SnapshotController
from binreconfiguration.overflowexception import OverflowException

class Overflow(Simulator):

	def run(self, strategy_factory, generator):
		"""Run this simulator.

		:param strategy_factory: The strategy class to be used by the simulator.
		:type strategy_factory: A concrete subclass of Strategy.
		"""
		# construct the bins
		bins = [Bin(self._capacity, "bin-{}.".format(i)) for i in range(self._number_of_bins)]

		# construct the (uniform) storage unit
		storage_unit = UniformStorageUnit(bins = bins, snapshots = SnapshotController())

		# 
		strategy = strategy_factory(storage_unit)

		# add items
		for item in generator:
			try:
				strategy.add_item(item)
			except OverflowException:
				return storage_unit.snapshots()
