from .strategy import Strategy
from .overflowexception import OverflowException

class FirstFit(Strategy):

	def add_item(self, item):
		self._add_item(item, enumerate(self._storage_unit))
