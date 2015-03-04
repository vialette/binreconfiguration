from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import AverageItemSize

class MinAverageItemSize(AscendingGaugedStrategy):

	def _gauge(self, item):
		return AverageItemSize(item)
