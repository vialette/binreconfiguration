"""Bin"""

from .binexception import BinException
from .snapshot import Snapshot

class Bin(object):

	def __init__(self, capacity, name = None):
		self._items    = []
		self._capacity = capacity
		self._name = name
		if self._name is None:
			self._name = "Bin-{}".format(id(self))

	def name(self):
		"""Return the name of this bin."""
		return self._name

	def capacity(self):
		"""Return the capacity of this bin."""
		return self._capacity

	def count(self):
		"""Return the number of items in this bin."""
		return len(self._items)

	def size(self):
		"""Return the total size of the items in this bin."""
		return sum(item for item in self._items)

	def free_space(self):
		"""Return the free space in this bin.

		The free space is the capacity of the bin minus the total size of the items
		in the bin.
		"""
		return self._capacity - self.size()

	def load(self):
		"""Return the load of this bin.

		The *load* of a bin is defined to be the ratio between the total size of the
		items in this bin and the capacity of this bin.
		"""
		return float(self.size()) / float(self.capacity())

	def __dir__(self):
		return ['capacity', 'count', 'size', 'free_space', 'load']

	def __getitem__(self, key):
		try:
			if key not in dir(self):
				raise AttributeError()
			fun = getattr(self, key)
			return fun()
		except AttributeError:
			raise BinException("unknown bin key")

	def add_item(self, item):
		"""Add an item to this bin.


		"""
		if item > self.free_space():
			raise BinException("Bin overflow")
		self._items.append(item)

	def __iter__(self):
		"""Iterate over the items in this bin.

		"""
		return iter(self._items)

	def __str__(self):
		"""Stringigy this bin.

		"""
		return str(self.snapshot())

	def snapshot(self):
		"""Return a snapshot of this bin."""
		return Snapshot(self)
