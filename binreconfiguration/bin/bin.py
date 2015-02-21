class BinException(Exception):
  
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)

class Bin(object):

	def __init__(self, capacity, name):
		self._capacity = capacity
		self._name     = name
		self._items    = []

	def capacity(self):
		return self._capacity

	def name(self):
		return self._name

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

	def remove_item(self, item):
		self._items.remove(item)

	def __iter__(self):
		return iter(self._items[:])

	def __str__(self):
		return ",".join(["(name={}, ".format(self._name),
						 "capacity={}, ".format(self._capacity),
						 "count={}, ".format(self.count()),
						 "size={})".format(self.size())])

	def snapshot(self):
		return {"count": self.count(), "size": self.size()}

class UnitBin(Bin):

	def __init__(self, name = None):
		super(UnitBin, self).__init__(1.0, name)