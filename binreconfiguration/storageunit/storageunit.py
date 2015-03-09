"""Storage unit"""

from .snapshot import Snapshot

class StorageUnit(object):

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
		"""Return the number of *bins* in this storage unit.

		"""
		return len(self._bins)

	def count(self):
		"""Return the number of *items* in the bins.

		"""
		return sum(bin.count() for bin in self._bins)

	def size(self):
		"""Return the total size of the items stored in the bins.


		"""
		return sum(bin.size() for bin in self._bins)

	def __iter__(self):
		"""Iteratate over the bins.

		"""
		return iter(self._bins)

	def items(self):
		"""Iterate over the items of the bins."""
		for bin in self._bins:
			for item in bin:
				yield item

	def filter(self, predicate):
		"""Filter the list of bins."""
		return [bin for bin in self._bin if predicate(bin)]

	def non_empty_bins(self):
		"""Return the list of all non-empty bins."""
		return self.filter(lambda bin: not bin.empty())

	def bins_with_freespace(self, freespace):
		"""Return the list of bins with at least *freespace* free space."""
		return self.filter(lambda bin: bin.free_space() >= free_space)

	def random_bin(self):
		"""Return a bin choosed at random."""
		return random.choice(self._bins)

	def random_nonempty_bin(self):
		"""Return a non-empty bin choosed at random."""
		return random.choice(self.non_empty_bins())

	def items(self):
		"""Return the list of all items stored in this storage unit."""
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
		"""Add an item to this storage unit."""
		self._bins[bin_index].add_item(item)
		if self._snapshots is not None:
			self._snapshots.add(self.snapshot())

	def clean_snapshots(self):
		"""Remove all stored snapshots."""
		if self._snapshots is not None:
			self._snapshots.clean()

	def snapshots(self):
		"""Return the snapshots of this storage unit.

		"""
		return self._snapshots

	def snapshot(self):
		"""Return the current snapshot of this storage unt.

		"""
		return Snapshot(self)


