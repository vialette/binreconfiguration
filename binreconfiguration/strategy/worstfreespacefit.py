from .descendinggaugedstrategy import DescendingGaugedStrategy
from .gauge import FreeSpace

class WorstFreeSpaceFit(DescendingGaugedStrategy):

	def _gauge(self, item):
		return FreeSpace(item)


