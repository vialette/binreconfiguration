from .Gaugedstrategy import GaugedStrategy
from .overflowexception import OverflowException

class DescendingGaugedStrategy(GaugedStrategy):

	def __init__(self, storage_unit):
		super(self.__class__, self).__init__(storage_unit)
		self._reverse = True