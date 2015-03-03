from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import FreeSpace

class MinFreeSpace(AscendingGaugedStrategy):

	def _gauge(self, item):
		return FreeSpace(item)


