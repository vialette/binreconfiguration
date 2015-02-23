from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import Count

class BestCountFit(AscendingGaugedStrategy):

	def _gauge(self, item):
		return Count(item)
