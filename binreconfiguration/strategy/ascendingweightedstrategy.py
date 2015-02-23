from .weightedstrategy  import WeightedStrategy
from .overflowexception import OverflowException

class AscendingWeightedStrategy(WeightedStrategy):

	def __init__(self, storage_unit):
		super(self.__class__, self).__init__(storage_unit)
		self._reverse = False