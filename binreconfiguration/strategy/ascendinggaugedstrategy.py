from .gaugedstrategy import GaugedStrategy

class AscendingGaugedStrategy(GaugedStrategy):

	def __init__(self, storage_unit):
		super(AscendingGaugedStrategy, self).__init__(storage_unit)
		self._reverse = False