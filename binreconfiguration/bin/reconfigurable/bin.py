import binreconfiguration.bin

class Bin(binreconfiguration.bin.Bin):

	def remove_item(self, item):
		self._bins[bin_index].remove_item(item)
