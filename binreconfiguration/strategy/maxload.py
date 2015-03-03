from .descendinggaugedstrategy import DescendingGaugedStrategy
from .gauge import Load

class MaxLoad(DescendingGaugedStrategy):

	def _gauge(self, item):
		return Load(item)


