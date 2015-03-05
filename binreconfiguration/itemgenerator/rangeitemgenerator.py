

class RangeItemGenerator(ItemGenerator):

	def __init__(self, lower_bound = 0.0, upper_bound = 1.0):
		self._lower_bound = lower_bound
		self._upper_bound = upper_bound