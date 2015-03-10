"""Simulator abstract base class.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

import abc

class Simulator(metaclass = abc.ABCMeta):

	def __init__(self, number_of_bins, capacity):
		"""

	    :param number_of_bins: The number of bins in this simulator.
	    :type number_of_bins: int.

		"""
		self._number_of_bins = number_of_bins
		self._capacity       = capacity

	@abc.abstractmethod
	def run(self):
		"""Run the simulator.

		Abstract method.
		
		"""
		pass