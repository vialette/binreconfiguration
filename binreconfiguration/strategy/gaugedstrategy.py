import abc

from .strategy import Strategy

class GaugedStrategy(Strategy):

	def add_item(self, item):
		gauge = self._gauge(item)
		indexed_items = sorted(enumerate(self._storage_unit), key = gauge, reverse = self._reverse)
		self._add_item(item, indexed_items)

	@abc.abstractmethod
	def _gauge(self, item):
		pass
