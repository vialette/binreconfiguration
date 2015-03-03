from .descendinggaugedstrategy import DescendingGaugedStrategy
from .gauge import FreeSpace

class MaxFreeSpace(DescendingGaugedStrategy):

	def _gauge(self, item):
		return FreeSpace(item)


