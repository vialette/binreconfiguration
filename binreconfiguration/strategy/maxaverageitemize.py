from .descendinggaugedstrategy import DescendingGaugedStrategy
from .gauge import FreeSpace

class MaxAverageItemSize(DescendingGaugedStrategy):

	def _gauge(self, item):
		return AverageItemSize(item)

