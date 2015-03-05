import abc
from binreconfiguration.overflowexception import OverflowException

class Strategy(metaclass = abc.ABCMeta):

	def __init__(self, storage_unit):
		self._storage_unit = storage_unit

	@abc.abstractmethod
	def add_item(self, item):
		pass

	def name(self):
		return self.__class__.__name__

	def _add_item(self, item, indexed_items):
		try:
			# find the smallest bin index of a bin with large enough free space
			index = next(index for (index, bin) in indexed_items if item <= bin.free_space())

			# add the item to the selected bin
			self._storage_unit.add_item(index, item)
		except StopIteration:
			raise OverflowException()

