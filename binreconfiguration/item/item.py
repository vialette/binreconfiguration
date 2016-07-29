"""ITem.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

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
