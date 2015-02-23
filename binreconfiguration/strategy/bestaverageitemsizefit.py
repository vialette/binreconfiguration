from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import AverageItemSize

class BestAverageItemSizeFit(AscendingGaugedStrategy):

	def _gauge(self, item):
		return AverageItemSize(item)
