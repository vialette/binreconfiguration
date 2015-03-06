import abc

class Explore(metaclass = abc.ABCMeta):

	def __init__(self, storage_unit):
		self._storage_unit = storage_unit

	def storage_unit(self):
		return self._storage_unit