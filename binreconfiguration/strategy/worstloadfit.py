from .descendinggaugedstrategy import DescendingGaugedStrategy
from .gauge import Load

class WorstLoadFit(DescendingGaugedStrategy):

	def _gauge(self, item):
		return Load(item)


