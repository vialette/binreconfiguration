"""Item generator base class"""

import abc
from binreconfiguration.item import Item

class ItemGenerator(metaclass = abc.ABCMeta):

	def __init__(self, lower_bound, upper_bound):
		self._lower_bound = lower_bound
		self._upper_bound = upper_bound

	@property
	def lower_bound(self):
		"""Return the lower bound of the item generator."""
		return self._lower_bound

	@property
	def upper_bound(self):
		"""Return the upper bound of the item generator."""
		return self._upper_bound

	@abc.abstractmethod
	def item(self):
		"""Return the next item provided by this item generator."""
		pass

	def __iter__(self):
		"""Yield items."""
		while True:
			yield Item(self.item())