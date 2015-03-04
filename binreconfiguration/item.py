
class Item(object):

	def __init__(self, value, name = None):
		self._value = value
		self._name = name
		if self._name is None:
			self._name = "{}-{}".format(self.__class__.__name__, id(self))

	def name(self):
		return self._name

	def value(self):
		return self._value

	def __float__(self):
		return float(self._value)

	def __add__(self, value):
		return self._value + value
		
	def __add__(self, value):
		return self._value + value

	def __radd__(self, value):
		return self._value + value

	def __sub__(self, value):
		return self._value - value

	def __rsub__(self, value):
		return value - self._value

	def __div__(self, value):
		return self._value / value

	def __rdiv__(self, value):
		return value / self._value

	def __floordiv__(self, value):
		return self._value / value

	def __rfloordiv__(self, value):
		return value / self._value

	def __mul__(self, value):
		return self._value * value

	def __rmul__(self, value):
		return value * self._value

	def __pow__(self, value):
		return pow(self._value, value)

	def __rpow__(self, value):
		return pow(value, self._value)

   	def __cmp__(self, value):
   		return cmp(self._value, value)

	def __str__(self):
		return str(self._value)

	def __int__(self):
		return int(self._value)