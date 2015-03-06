"""Simulator abstract base class"""

import abc

class Simulator(metaclass = abc.ABCMeta):

	def __init__(self, number_of_bins, capacity):
		self._number_of_bins = number_of_bins
		self._capacity       = capacity

	@abc.abstractmethod
	def run(self):
		"""Run the simulator."""
		pass