"""Storage unit"""

from .snapshot import Snapshot

class StorageUnit(object):

	def __init__(self, bins = None, snapshots = None, name = None):
		if bins is None:
			self._bins = []
		else:
			self._bins = bins[:]
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
		"""Iterator over the bins.

		"""
		return iter(self._bins)

	def __getitem__(self, bin_index):
		"""Access to bin *bin_index*.

		"""
		return self._bins[bin_index]

	def __str__(self):
		"""Return a string representation of this storage unit.


		"""
		return ",".join([str(bin) for bin in self._bins])

	def add_item(self, bin_index, item):
		self._bins[bin_index].add_item(item)
		if self._snapshots is not None:
			self._snapshots.add(self.snapshot())

	def snapshots(self):
		"""Return the snapshots of this storage unit.

		"""
		return self._snapshots

	def snapshot(self):
		"""Return the current snapshot of this storage unt.

		"""
		return Snapshot(self)


