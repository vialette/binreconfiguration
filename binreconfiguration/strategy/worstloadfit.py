from .descendingGaugedstrategy import DescendingGaugedStrategy
from .gauge import Load

class WorstLoadFit(DescendingGaugedStrategy):

	@staticmethod
	def _weight(item):
		return Load(item)


