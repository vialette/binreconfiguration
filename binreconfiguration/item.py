import copy

class Item(object):

	# the current timestamp of the class
	_timestamp = 0

	def __init__(self, value, name = None):
		self._value = value
		self._name  = name
		if self._name is None:
			self._name = "{}-{}".format(self.__class__.__name__, id(self))
		self.__class__._timestamp += 1
		self._timestamp = self.__class__._timestamp

	def copy(self):
		"""Return a deep copy af this item.


		The timestamp of the new item is equal to the timestamp of the copied item.
		"""
		return copy.deepcopy(self)

	def name(self):
		"""Return the name of this item.

		"""
		return self._name

	def value(self):
		"""Return the value of this item.

		"""
		return self._value

	def timestamp(self):
		"""Return the timestamp of this item.

		"""
		return self._timestamp

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

	def __truediv__(self, value):
		return self._value / value

	def __rtruediv__(self, value):
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

	def __eq__(self, value):
		return self._value == value

	def __ne__(self, value):
		return self._value != value

	def __lt__(self, value):
		return self._value < value

	def __gt__(self, value):
		return self._value > value

	def __le__(self, value):
		return self._value <= value

	def __ge__(self, value):
		return self._value >= value

	def __str__(self):
		return str(self._value)

	def __int__(self):
		return int(self._value)

	def __float__(self):
		return float(self._value)