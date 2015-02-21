from .strategy import Strategy

class firstFit(Strategy):

	def add_item(self, item):
		try:
			index = next(index for (index, bin) in enumerate(self._storage) if bin.free_space() >= item)
			self._storage.add_item(bin, index)
		except StopIteration:
			raise binreconfiguration.OverflowException()