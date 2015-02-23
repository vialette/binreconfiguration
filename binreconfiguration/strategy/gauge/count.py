from .gauge import Gauge

class Count(Gauge):

	def __call__(self, t):
		(_, bin) = t
		return bin.count() + 1