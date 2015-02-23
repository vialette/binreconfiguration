from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import Load

class BestLoadFit(AscendingGaugedStrategy):

	def _gauge(self, item):
		return Load(item)
