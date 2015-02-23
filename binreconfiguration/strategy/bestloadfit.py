from .ascendingweightedstrategy import AscendingWeightedStrategy

class BestLoadFit(AscendingWeightedStrategy):

	# ascending sort bin according to load
	def _weight(item):
		return _load(item)

