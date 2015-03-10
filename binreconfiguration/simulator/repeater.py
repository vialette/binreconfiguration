"""Simulator repeater.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

class Repeater(object):

	def __init__(self, simulator):
		"""Initialize this silumator repeater.

	    :param simulator: The simulator to be repeated.
	    :type simulator: Simulator.

		"""
		self._simulator = simulator

	def run(self, strategy, generator, number_of_simulations):
		"""Run the simulator inside the repeater.

	    :param strategy: The insertion strategy.
	    :type strategy: Strategy.
	    :param generator: An item generator.
	    :type name: Generator.
	    :param number_of_simulations: The number of simulations.
	    :type number: int.
	    :returns:  list -- the list of all simulation's results.

		"""
		return [self._simulator.run(strategy, generator).last()
				for _ in range(number_of_simulations)]
