from .descendingweightedstrategy import DescendingWeightedStrategy

class WorstLoadFit(DescendingWeightedStrategy):

	# descending sort bin according to load
	def _weight(item):
		return _load(item)


