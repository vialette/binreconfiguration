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
		return self._name

	def capacity(self):
		return self._capacity

	def count(self):
		return len(self._items)

	def size(self):
		return sum(item for item in self._items)

	def free_space(self):
		return self._capacity - self.size()

	def load(self):
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
		if item > self.free_space():
			raise BinException("Bin overflow")
		self._items.append(item)

	def __iter__(self):
		return iter(self._items)

	def __str__(self):
		return str(self.snapshot())

	def snapshot(self):
		return Snapshot(self)
