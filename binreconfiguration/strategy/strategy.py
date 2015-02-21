import abc

class Strategy(metaclass = abc.ABCMeta):

	def __init__(self, storage):
		self._storage = storage

  	@abstractmethod
	def add_item(self, item):
		pass