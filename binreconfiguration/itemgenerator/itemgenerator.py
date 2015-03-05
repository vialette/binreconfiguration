import abc
from binreconfiguration.item import Item

class ItemGenerator(object):

	def __init__(self, lower_bound, upper_bound):
		self._lower_bound = lower_bound
		self._upper_bound = upper_bound


	@property
	def lower_bound(self):
		return self._lower_bound

	@property
	def upper_bound(self):
		return self._upper_bound

	@abc.abstractmethod
	def item(self):
		pass

	def __iter__(self):
		while True:
			yield Item(self.item())