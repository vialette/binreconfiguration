from .gauge import Gauge

class Load(Gauge):

	def __call__(self, t):
		(_, bin) = t
		return (bin.size() + self._item) / bin.capacity()