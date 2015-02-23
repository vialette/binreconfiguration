from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import Load

class BestLoadFit(AscendingGaugedStrategy):

	def _gauge(item):
		return Load(item)
