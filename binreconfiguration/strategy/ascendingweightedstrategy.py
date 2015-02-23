from .strategy import Strategy
from .overflowexception import OverflowException

class AscendingWeightedStrategy(Strategy):

	def add_item(self, item):
		indexed_items = sorted(enumerate(self._storage_unit), key = self._weight(item))
		try:
			index = next(index for (index, bin) in indexed_items if bin.free_space() >= item)
			print("index = {}".format(index))
			self._storage_unit.add_item(index, item)
		except StopIteration:
			raise OverflowException()