"""Count gauge"""

from .gauge import Gauge

class Count(Gauge):

	def __call__(self, t):
		"""Return the number of items in a bin (including the requested one)."""
		(_, bin) = t
		return bin.count() + 1