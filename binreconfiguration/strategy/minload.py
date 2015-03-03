from .ascendinggaugedstrategy import AscendingGaugedStrategy
from .gauge import Load

class MinLoad(AscendingGaugedStrategy):

	def _gauge(self, item):
		return Load(item)
