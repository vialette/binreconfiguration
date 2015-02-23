

class StorageUnit(object):

	def __init__(self, name = None):
		self._bins = []
		self._name = name
		if self._name is None:
			self._name = "{} {}".format(self.__class__.__name__, id(self))

	def add_bins(self, bins):
		for bin in bins:
			self.add_bin(bin)

	def add_bin(self, bin):
		self._bins.append(bin)

	def remove_bin(self, bin):
		self._bins.remove(bin)

	def __len__(self):
		return len(self._bins)

	def count(self):
		return sum(bin.count() for bin in self._bins)

	def size(self):
		return sum(bin.size() for bin in self._bins)

	def __iter__(self):
		return iter(self._bins)

	def __getitem__(self, bin_index):
		return self._bins[bin_index]

	def __str__(self):
		return ",".join([str(bin) for bin in self._bins])

	def add_item(self, bin_index, item):
		self._bins[bin_index].add_item(item)

	def snapshot(self):
		return tuple(bin.snapshot() for bin in self._bins)


