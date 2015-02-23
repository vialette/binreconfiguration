import binreconfiguration.storageunit

class StorageUnit(binreconfiguration.storageunit.StorageUnit):

	def remove_item(self, bin_index, item):
		self._bins[bin_index].remove_item(item)

	def move_item(self, from_bin_index, to_bin_index, item):
		self.remove_item(from_bin_index, item)
		self.add_item(to_bin_index, item)