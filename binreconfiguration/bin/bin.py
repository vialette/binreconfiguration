from .binexception import BinException
from .snapshot import Snapshot

class Bin(object):

	def __init__(self, capacity, name = None):
		self._items    = []
		self._capacity = capacity
		self._name = name
		if self._name is None:
			self._name = "Bin {}".format(id(self))

	def name(self):
		return self._name

	def capacity(self):
		return self._capacity

	def count(self):
		return len(self._items)

	def size(self):
		return sum(item for item in self._items)

	def free_space(self):
		return self._capacity - self.size()

	def add_item(self, item):
		if item > self.free_space():
			raise BinException("Bin overflow")
		self._items.append(item)

	def __iter__(self):
		return iter(self._items[:])

	def __str__(self):
		return ",".join(["(name={}, ".format(self._name),
						 "capacity={}, ".format(self._capacity),
						 "count={}, ".format(self.count()),
						 "size={})".format(self.size())])

	def snapshot(self):
		return Snapshot(self._count, self._size}

