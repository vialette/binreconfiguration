from .ascendingGaugedstrategy import AscendingGaugedStrategy
from .gauge import Load

class BestLoadFit(AscendingGaugedStrategy):

	def _weight(item):
		return Load(item)
