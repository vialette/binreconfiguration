"""Storage unit.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

from .snapshot import Snapshot
import pickle

class StorageUnit(object):
	"""Stogae unit.

	"""

	def __init__(self, bins = None, snapshots = None, name = None):
		if bins is None:
			self._bins = []
		else:
			self._bins = [bin for bin in bins]
		self._name = name
		if self._name is None:
			self._name = "{}-{}".format(self.__class__.__name__, id(self))
		self._snapshots = snapshots

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
		"""Iteratate over the bins of this storage unit.
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
		return [bin for bin in self._bin if predicate(bin)]

	def non_empty_bins(self):
		"""Return the list of all non-empty bins.
		"""
		return self.filter(lambda bin: not bin.empty())

	def bins_with_free_space(self, free_space):
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
		if self._snapshots is not None:
			self._snapshots.add(self.snapshot())

	def clean_snapshots(self):
		"""Remove all stored snapshots of this stroage unit.
		"""
		if self._snapshots is not None:
			self._snapshots.clean()

	def snapshots(self):
		"""Return the list of all snapshots of this storage unit.
		"""
		return self._snapshots

	def snapshot(self):
		"""Return the snapshot of this storage unt.
		"""
		return Snapshot(self)

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