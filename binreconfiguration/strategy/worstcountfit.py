from .descendinggaugedstrategy import DescendingGaugedStrategy
from .gauge import Count

class WorstCountFit(DescendingGaugedStrategy):

	def _gauge(self, item):
		return Count(item)
