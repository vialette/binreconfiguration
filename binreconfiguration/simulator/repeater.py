"""Simulator repeater"""

class Repeater(object):

	def __init__(self, simulator):
		self._simulator = simulator

	def run(self, strategy, generator, number_of_simulations):
		return [self._simulator.run(strategy, generator).last()
				for _ in range(number_of_simulations)]
