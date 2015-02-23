import abc

class Strategy(metaclass = abc.ABCMeta):

	def __init__(self, storage_unit):
		self._storage_unit = storage_unit

	@abc.abstractmethod
	def add_item(self, item):
		pass

	def _add_item(self, item, indexed_items):
		print("Strategy._add_item. indexed_items={}".format(indexed_items))
		try:
			index = next(index for (index, bin) in indexed_items if bin.free_space() >= item)
			self._storage_unit.add_item(index, item)
		except StopIteration:
			raise OverflowException()

