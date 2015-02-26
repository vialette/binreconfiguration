from .binexception import BinException
from .snapshot import Snapshot

class Bin(object):

	_NAME       = 'name'
	_CAPACITY   = 'capacity'
	_COUNT      = 'count'
	_SIZE       = 'size'
	_FREE_SPACE = 'free_space'

	def __init__(self, capacity, name = None):
		self._items    = []
		self._capacity = capacity
		self._name = name
		if self._name is None:
			self._name = "Bin-{}".format(id(self))

	def keys(self):
		return [self._NAME, self._CAPACITY, self._COUNT, self._SIZE, self._FREE_SPACE]

	def dyn_keys(self):
		return [self._COUNT, self._SIZE, self._FREE_SPACE]

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

	def __getitem__(self, key):
		if key == 'name':
			return self._name
		elif key == 'capacity':
			return self._capacity
		elif key == 'count':
			return self.count()
		elif key == 'size':
			return self.size()
		elif key == 'free_space':
			return self.free_space()
		else:
			raise BinException("unknown bin key")

	def __iter__(self):
		return iter(self._items[:])

	def __str__(self):
		return str(self.snapshot())

	def snapshot(self):
		return Snapshot(self)

	def dyn_snapshot(self):
		return Snapshot(self, self.dyn_keys())