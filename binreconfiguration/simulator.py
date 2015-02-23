from binreconfiguration.bin import Bin
from binreconfiguration.storageunit import SnapshotedStorageUnit

class Simulator(object):

	def __init__(self, number_of_bins, capacity):
		self._number_of_bins = number_of_bins
		self._capacity       = capacity

	def _setup_bins(self):
		self._bins = [Bin(self._capacity) for _ in range(self._number_of_bins)]

	def _setup_storage_unit(self):
		self._storage_unit = SnapshotedStorageUnit()
		self._storage_unit.add_bins(self._bins)

	def _setup_contrete_strategy(self):
		self._strategy = self._strategy_factory(self._storage_unit)
	
	def _setup(self):
		self._setup_bins()
		self._setup_storage_unit()
		self._setup_contrete_strategy()

	def run(self, strategy_factory, items):
		self._strategy_factory = strategy_factory
		self._setup()
		for item in items():
			try:
				self._strategy.add_item(item)
			except Exception:
				return  self._storage_unit.snapshots()
