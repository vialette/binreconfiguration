from .bin import Bin

class UnitBin(Bin):

	def __init__(self, name = None):
		super(UnitBin, self).__init__(1.0, name)