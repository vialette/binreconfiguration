class Repeater(object):

	def __init__(self, simulator, strategy, generator, number_of_simulations):
		self._simulator = simulator
		self._strategy  = strategy
		self._generator = generator
		self._number_of_simulations = number_of_simulations

	def run(self):
		return [simulator.run(self._strategy, self._simulator).last()
				for _ in range(self._number_of_simulations)]
