from .descendinggaugedstrategy import DescendingGaugedStrategy
from .gauge import Count

class MaxCount(DescendingGaugedStrategy):

	def _gauge(self, item):
		return Count(item)
