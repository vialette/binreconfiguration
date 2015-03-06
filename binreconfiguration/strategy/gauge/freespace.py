"""Free space gauge"""

from .gauge import Gauge

class FreeSpace(Gauge):

	def __call__(self, t):
		"""Return the free space in a bin (taking into account the requested item)."""
		(_, bin) = t
		return bin.free_space() - self._item