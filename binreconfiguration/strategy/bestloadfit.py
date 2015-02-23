from .ascendingweightedstrategy import AscendingWeightedStrategy
from .gauge import Load

class BestLoadFit(AscendingWeightedStrategy):

	def _weight(item):
		return Load(item)
