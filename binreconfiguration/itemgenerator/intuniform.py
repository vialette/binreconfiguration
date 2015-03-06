"""Item generator: integer uniform distribution"""

from .itemgenerator import ItemGenerator
import random

class IntUniform(ItemGenerator):

	def __init__(self, lower_bound, upper_bound):
		self._lower_bound = lower_bound
		self._upper_bound = upper_bound

	def item(self):
		"""Return a random integer.


		"""
		return random.randint(self._lower_bound, self._upper_bound)

