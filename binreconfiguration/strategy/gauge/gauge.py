import abc

class Gauge(metaclass = abc.ABCMeta):

	def __init__(self, item):
		self._item = item

	@abc.abstractmethod
	def __call__(self, bin):
		pass