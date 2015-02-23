from .gauge import Gauge

class FreeSpace(Gauge):

	def __call__(self, t):
		(_, bin) = t
		return bin.free_space()