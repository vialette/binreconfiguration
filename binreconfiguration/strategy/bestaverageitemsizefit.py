from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import AverageItemSize

class BestAverageIteSizeFit(AscendingGaugedStrategy):

	def _gauge(self, item):
		return AverageItemSize(item)
