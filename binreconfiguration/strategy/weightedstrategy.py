import abc

from .strategy import Strategy
from .overflowexception import OverflowException

class WeightedStrategy(Strategy):

	def add_item(self, item):
		print("WeightedStrategy. avant sorted")
		indexed_items = sorted(list(enumerate(self._storage_unit)), 
							   key = self._weight(item), reverse = self._reverse)
		print("WeightedStrategy. apres sorted")
		self._add_item(item, indexed_items)

	@abc.abstractmethod
	def _weight(self):
		pass

	@staticmethod
	def _load(item):
		def _inner(t):
			(_, bin) = t
			return (bin.size() + item) / bin.capacity()
		return _inner

	@staticmethod
	def _count(item):
		def _inner(t):
			(_, bin) = t
			return bin.count()
		return _inner

	@staticmethod
	def _free_space(item):
		def _inner(t):
			(_, bin) = t
			return bin.free_space()
		return _inner

	@staticmethod
	def _average_item_size(item):
		def _inner(t):
			(_, bin) = t
			return (bin.size() + item) / bin.count()
		return _inner	