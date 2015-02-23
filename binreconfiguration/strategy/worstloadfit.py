from .descendingweightedstrategy import DescendingWeightedStrategy
from .gauge import Load

class WorstLoadFit(DescendingWeightedStrategy):

	@staticmethod
	def _weight(item):
		return Load(item)


