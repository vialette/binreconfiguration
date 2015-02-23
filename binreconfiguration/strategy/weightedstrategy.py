import abc

from .strategy import Strategy
from .overflowexception import OverflowException

class WeightedStrategy(Strategy):

	def add_item(self, item):
		key_fun = self._weight(item)
		indexed_items = sorted(enumerate(self._storage_unit), key = key_fun, reverse = self._reverse)
		self._add_item(item, indexed_items)

	@abc.abstractmethod
	def _weight(self):
		pass
