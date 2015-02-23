from .descendinggaugedstrategy import DescendingGaugedStrategy
from .gauge import AverageItemSize

class WorstAverageItemSizeFit(DescendingGaugedStrategy):

	def _gauge(self, item):
		return AverageItemSize(item)
