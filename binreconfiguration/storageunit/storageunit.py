"""Storage unit module.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

from .snapshot import Snapshot
from .storageunitexception import StorageUnitException
import pickle

class StorageUnit(object):
	"""Storage unit.

	"""

	def __init__(self, bins = None, snapshots = None, name = None, regular = True, dynamic = False):
		# regular
		self._regular = regular
		if self._regular and bins != []:
			capacities = [bin.capacity() for bin in bins]
			if capacities.count(capacities[0]) != len(capacities):
				raise StorageUnitException("distinct bin capacities in regular storage unit")

		# dynamic
		self.dynamic = dynamic

		# bins
		if bins is None:
			self._bins = []
		else:
			self._bins = [bin for bin in bins]

		# name
		self._name = name
		if self._name is None:
			self._name = "{}-{}".format(self.__class__.__name__, id(self))

		# snapshot controller
		self._snapshot_controller = snapshots

	def __len__(self):
		"""Return the number of bins in this storage unit.
		"""
		return len(self._bins)

	def count(self):
		"""Return the number of items in the bins of this storage unit.
		"""
		return sum(bin.count() for bin in self._bins)

	def size(self):
		"""Return the total size of the items stored in the bins of this storage unit.
		
		"""
		return sum(bin.size() for bin in self._bins)

	def __iter__(self):
		"""Iterate over the bins of this storage unit.

		"""
		return iter(self._bins)

	def items(self):
		"""Iterate over the items of the bins of this storage unit.
		"""
		for bin in self._bins:
			for item in bin:
				yield item

	def filter(self, predicate):
		"""Filter the list of bins.

	    :param predicate: The function predicate to filter the bins.
	    :type predicate: function.

		"""
		return (bin for bin in self.bins if predicate(bin))

	def non_empty_bins(self):
		"""Return the non-empty bins of this storage unit.
		"""
		return self.filter(lambda bin: not bin.empty())

	def empty_bins(self):
		"""Return the empty bins of this storage unit.
		"""
		return self.filter(lambda bin: bin.empty())

	def large_enough_bins(self, free_space):
		"""Return the list of bins with large enough free space.

	    :param free_space: The needed free space.
	    :type free_space: Numeric.

		"""
		return self.filter(lambda bin: bin.free_space() >= free_space)

	def random_bin(self):
		"""Return a bin choosed at random.

		:raises: IndexError

		"""
		return random.choice(self._bins)

	def random_nonempty_bin(self):
		"""Return a non-empty bin choosed at random.

		:raises: IndexError

		"""
		return random.choice(self.non_empty_bins())

	def items(self):
		"""Return the list of all items stored in this storage unit.
		"""
		return [item for bin in self._bins for item in bin]

	def __getitem__(self, bin_index):
		"""Access to bin *bin_index*.

		"""
		return self._bins[bin_index]

	def __str__(self):
		"""Return a string representation of this storage unit.
		"""
		return ",".join([str(bin) for bin in self._bins])

	def add_item(self, bin_index, item):
		"""Add an item to this storage unit.

	    :param bin_index: The index of the bin that should accomodate the item.
	    :type bin_index: int.
	    :param item: The item to add.
	    :type item: Item.
	    :raises: IndexError

		"""
		self._bins[bin_index].add_item(item)
		if self._snapshot_controller is not None:
			self._snapshot_controller.add(self.snapshot())

	def clean_snapshot_controller(self):
		"""Remove all stored snapshots of this stroage unit.
		"""
		if self._snapshot_controller is not None:
			self._snapshot_controller.clean()

	def snapshots(self):
		"""Return the list of all snapshots of this storage unit.
		"""
		return self._snapshot_controller

	def snapshot(self):
		"""Return the snapshot of this storage unit.
		"""
		return Snapshot(self)

	def dynamic(self):
		"""Return True if this storage unit is dynamic, and False otherwise.
		"""
		return self._dynamic

	def set_dynamic(self):
		"""Make this storage unit dynamic.
		"""
		self._dynamic = True

	def set_non_dynamic(self):
		"""Make this storage unit non-dynamic.
		"""
		self._dynamic = False

	def add_bin(self, bin):
		"""Add one bin to this this storage unit.


		"""
		# only dynamic storage units can gain a new bin
		if not self._dynamic:
			raise StorageUnitException("adding bin to an non-dynamic storage unit")
		self._bins.append(bin)

		# let the snapshot storage unit controller knows about this new bin
		if self._snapshot_controller is not None:
			self._snapshot_controller.add(self.snapshot())

	def remove_bin(self, bin):
		"""Remove one bin from this storage unit.


		"""
		# only dynamic storage units can loose a bin
		if not self._dynamic:
			raise StorageUnitException("removing bin from an non-dynamic storage unit")
		self._bins.remove(bin)

		# let the snapshot storage unit controller knows about this lost bin
		if self._snapshot_controller is not None:
			self._snapshot_controller.add(self.snapshot())

	def dump(self, filename):
		"""Dump this storage unit.

	    :param filename: The filename of the pickle file.
	    :type filename: str.

		"""
		with open(filename, 'wb') as f:
			pickle.dump(self, f)

	@staticmethod
	def load(self, filename):
		"""Load a storage unit from a pickle file.

	    :param filename: The filename of the pickle file.
	    :type filename: str.

		"""
		storage_unit = None
		with open(filename, 'wb') as f:
			storage_unit = pickle.load(f)
		return storage_unit
