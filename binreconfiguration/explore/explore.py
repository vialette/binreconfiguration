import abc

class Explore(metaclass = abc.ABCMeta):

	def __init__(self, storage_unit):
		self._storage_unit = storage_unit
		self._number_of_steps = 0

	def storage_unit(self):
		return self._storage_unit

	def number_of_steps(self):
		return self._number_of_steps

	@abc.abstractmethod
	def run(fitness_fun):
		pass