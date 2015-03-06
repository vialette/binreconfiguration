"""Average item size gaucge"""

from .gauge import Gauge

class AverageItemSize(Gauge):

	def __call__(self, t):
		"""Return the average item size in a bin (taking into account the item to be inserted).""" 
		(_, bin) = t
		return float(bin.size() + self._item) / bin.count()