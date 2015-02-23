from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import FreeSpace

class BestFreeSpaceFit(AscendingGaugedStrategy):

	def _gauge(self, item):
		return FreeSpace(item)


