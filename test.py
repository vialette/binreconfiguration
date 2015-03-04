

class A(object):

	def __init__(self, value = 0):
		self._value = value

	def __int__(self):
		print("A.__int__")
		return int(self._value)

	def __float__(self):
		return float(self._value)

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

a = A(7.0)
b = A(3)

print("a = {}".format(a))
print("b = {}".format(b))
print("\n")
print("a + b = {}".format(a + b))
print("b + a = {}".format(b + a))
print("a + 10 = {}".format(a + 10))
print("10 + a = {}".format(10 + a))
print("\n")
print("a - b = {}".format(a - b))
print("b - a = {}".format(b - a))
print("a - 10 = {}".format(a - 10))
print("10 - a = {}".format(10 - a))
print("\n")
print("a / b = {}".format(a / b))
print("b / a = {}".format(b / a))
print("a / 10 = {}".format(a / 10))
print("10 / a = {}".format(10 / a))
print("\n")
print("float(a) / b = {}".format(float(a) / b))
print("a / float(b) = {}".format(a / float(b)))
print("float(a) / float(b) = {}".format(float(a) / float(b)))
print("float(a) / 10 = {}".format(float(a) / 10))
print("a / 10.0 = {}".format(a / 10.0))
print("float(a) / 10.0 = {}".format(float(a) / 10.0))
print("10 / float(a) = {}".format(10 / float(a)))
print("10.0 / a = {}".format(10.0 / a))
print("10.0 / float(a) = {}".format(10.0 / float(a)))
print("\n")
print("a // b = {}".format(a // b))
print("b // a = {}".format(b // a))
print("a // 10 = {}".format(a // 10))
print("10 // a = {}".format(10 // a))
print("\n")
print("a * b = {}".format(a * b))
print("b * a = {}".format(b * a))
print("a * 10 = {}".format(a * 10))
print("10 * a = {}".format(10 * a))
print("\n")
print("pow(a, b) = {}".format(pow(a, b)))
print("pow(b, a) = {}".format(pow(b, a)))
print("pow(a, 3) = {}".format(pow(a, 3)))
print("pow(3, a) = {}".format(pow(3, a)))
print("\n")
print("cmp(a, b) = {}".format(cmp(a, b)))
print("cmp(b, a) = {}".format(cmp(b, a)))
print("\n")
print("int(a) = {}".format(int(a)))
print("float(a) = {}".format(float(a)))