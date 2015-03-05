from .itemgenerator import ItemGenerator
import random

class Uniform(ItemGenerator):

	def __init__(self, lower_bound = 0.0, upper_bound = 1.0):
		super(self.__class__, self).__init__(lower_bound, upper_bound)

	def item(self):
		return random.uniform(self.lower_bound, self.upper_bound)

