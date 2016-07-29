"""Items

"""

import operator
import random

class Items(object):

	def __init__(self, items):
		self._items = items

	def items_with_size(self, size):
		return [item for item in self._items if item.size() == size]

	def smallest_size_item(self):
		return min(self._items, key = operator.attrgetter('size'))

	def smallest_size_items(self):
		smallest_size = self.smallest_size_item().size()
		return [item for item in self._items if item.size() == smallest_size]

	def largest_size_item(self):
		return max(self._items, key = operator.attrgetter('size'))

	def largest_size_items(self):
		largest_size = self.largest_size_item().size()
		return [item for item in self._items if item.size() == largest_size]

	def items_with_ascending_size(self):
		return sorted(self._items, key = operator.attrgetter('size'))

	def items_with_descending_size(self):
		return sorted(self._items, key = operator.attrgetter('size'), reverse = True)

	def items_with_timestamp(self, timestamp):
		return [item for item in self._items if item.timestamp() == timestamp]

	def oldest_timestamp_item(self):
		return min(self._items, key = operator.attrgetter('timestamp'))

	def oldest_timestamp_items(self):
		oldest_timestamp = self.oldest_timestamp_item().timestamp()
		return [item for item in self._items if item.timestamp() == oldest_timestamp]

	def recentest_timestamp(self):
		return max(self._items, key = operator.attrgetter('size'))

	def recentest_timestamp_items(self):
		recentest_timestamp = self.recentest_timestamp_item().timestamp()
		return [item for item in self._items if item.timestamp() == recentest_timestamp]

	def items_with_ascending_timestamp(self):
		return sorted(self._items, key = operator.attrgetter('timestamp'))

	def items_with_descending_timestamp(self):
		return sorted(self._items, key = operator.attrgetter('timestamp'), reverse = True)

	def shuffle(self):
		shuffled_items = random.shuffle(self._items)
		return shuffled_items

	def random(self):
		return random.choice(self._items)