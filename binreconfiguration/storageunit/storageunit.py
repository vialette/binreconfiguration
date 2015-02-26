from .snapshot import Snapshot

class StorageUnit(object):

	def __init__(self, bins = None, snapshot_controller = None, name = None):
		if bins is None:
			self._bins = []
		else:
			self._bins = bins[:]
		self._name = name
		if self._name is None:
			self._name = "{}-{}".format(self.__class__.__name__, id(self))
		self._snapshot_controller = snapshot_controller

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
		if self._snapshot_controller is not None:
			self._snapshot_controller.append(self.snapshot())

	def snapshot_controller(self):
		return self._snapshot_controller

	def snapshot(self):
		return Snapshot(self)


