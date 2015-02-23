import random

from .strategy import Strategy

class RandomFit(Strategy):

	def add_item(self, item):
		indexed_items = list(enumerate(self._storage_unit))
		random.shuffle(indexed_items)
		self._add_item(item, indexed_items)