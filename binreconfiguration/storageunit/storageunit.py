

class StorageUnit(object):

	def __init__(self, name = None):
		self._name = name
		self._bins = []

	def add_bin(self, bin):
		self._bins.append(bin)

	def remove_bin(self, bin):
		self._bins.remove(bin)

	def __len__(self):
		return self._nb_bins

	def count(self):
		return sum(bin.count() for bin in self._bins)

	def size(self):
		return sum(bin.size() for bin in self._bins)

	def __iter__(self):
		return iter(self._bins)

	def __getitem__(self, i):
		return self._bins[i]

	def __str__(self):
		return ",".join([str(bin) for bin in self._bins])

	def add_item(self, index, item):
		self._bins[index].add_item(item)

	def snapshot(self):
		return tuple(bin.snapshot() for bin in self._bins)


