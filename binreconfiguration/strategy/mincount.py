from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import Count

class MinCount(AscendingGaugedStrategy):

	def _gauge(self, item):
		return Count(item)
