"""Gauge base class"""

import abc

class Gauge(metaclass = abc.ABCMeta):

	def __init__(self, item):
		"""Initialize this gauge;


	    :param item: The gauged item..
	    :type item: Item.
		"""
		self._item = item

	@abc.abstractmethod
	def __call__(self, t):
		pass