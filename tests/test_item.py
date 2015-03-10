from binreconfiguration import Item
import re

class TestItem_Timestamp(object):

	def setup(self):
		self.item1 = Item(1)
		self.item2 = Item(2)

	def test_increment(self):
		assert self.item2.timestamp() == self.item1.timestamp() + 1

	def test_copy_does_not_modify_timestamp(self):
		assert self.item1.copy().timestamp() == self.item1.timestamp()
		assert self.item2.copy().timestamp() == self.item2.timestamp()

	def test_restart_increment(self):
		item3 = Item(3)
		assert item3.timestamp() == self.item2.timestamp() + 1

# content of test_class.py
class TestItem(object):
	def setup(self):
		self.item = Item(100)

	def test_copy(self):
		item = self.item.copy()
		assert item == 100
		assert id(self.item) != item

	def test_no_name(self):
		pattern = re.compile('^Item-(\d)+$')
		assert pattern.match(self.item.name())

	def test_name(self):
		item = Item(100, "my item")
		assert item.name() == "my item"

	def test_value(self):
		assert self.item.value() == 100
		assert isinstance(self.item.value(), int)

	def test_add_value(self):
		assert self.item + 101 == 100 + 101
		assert isinstance(self.item + 101, int)

	def test_radd_value(self):
		assert 101 + self.item == 101 + 100
		assert isinstance(101 + self.item, int)

	def test_add_item(self):
		assert self.item + Item(101) == 100 + 101
		assert isinstance(self.item + Item(101), int)

	def test_sub_value(self):
		assert self.item - 1 == 99
		assert isinstance(self.item - 1, int)

	def test_rsub_value(self):
		assert 101 - self.item == 1
		assert isinstance(101 - self.item, int)

	def test_sub_item(self):
		assert self.item - Item(99) == 1
		assert isinstance(self.item - Item(99), int)

	def test_mul_value(self):
		assert self.item * 10 == 100 * 10
		assert isinstance(self.item * 10, int)

	def test_rmul_value(self):
		assert 10 * self.item == 10 * 100
		assert isinstance(10 * self.item, int)

	def test_mul_item(self):
		assert self.item * Item(10) == 100 * 10
		assert isinstance(self.item * Item(100), int)

	def test_truediv_value(self):
		assert self.item / 8 == 12.5
		assert isinstance(self.item / 4, float)

	def test_rtruediv_value(self):
		assert 110 / self.item == 1.1
		assert isinstance(110 / self.item, float)

	def test_truediv_item(self):
		assert self.item / Item(8) == 12.5
		assert isinstance(self.item / Item(8), float)

	# def test_floordiv_value(self):
	# 	assert self.item // 3 == 33
	# 	assert isinstance(self.item // 3, int)

	# def test_rfloordiv_value(self):
	# 	assert 110 // self.item == 1
	# 	assert isinstance(110 // self.item, int)

	# def test_floordiv_item(self):
	# 	assert self.item // Item(3) == 33
	# 	assert isinstance(self.item // Item(3), int)

	def test_pow_value(self):
		assert self.item ** 2 == 100 ** 2
		assert isinstance(self.item ** 2, int)

	def test_rpow_value(self):
		assert 2 ** self.item == 2 ** 100
		assert isinstance(10 * self.item, int)

	def test_pow_item(self):
		assert self.item ** Item(2) == 100 ** 2
		assert isinstance(self.item * Item(2), int)

	def test_le_value(self):
		assert not (self.item <= 99)
		assert self.item <= 100
		assert self.item <= 101

	def test_le_item(self):
		assert not (self.item <= Item(99))
		assert self.item <= Item(100)
		assert self.item <= Item(101)

	def test_lt_value(self):
		assert not (self.item < 99)
		assert not (self.item < 100)
		assert self.item < 101

	def test_lt_item(self):
		assert not (self.item < Item(99))
		assert not (self.item < Item(100))
		assert self.item < Item(101)

	def test_ge_value(self):
		assert not (self.item >= 101)
		assert self.item >= 100
		assert self.item >= 99

	def test_ge_item(self):
		assert not (self.item >= Item(101))
		assert self.item >= Item(100)
		assert self.item >= Item(99)

	def test_gt_value(self):
		assert not (self.item > 101)
		assert not (self.item > 100)
		assert self.item > 99

	def test_gt_item(self):
		assert not (self.item > Item(101))
		assert not (self.item > Item(100))
		assert self.item > Item(99)

	def test_eq_value(self):
		assert self.item == 100
		assert 100 == self.item

	def test_eq_item(self):
		assert self.item == Item(100)

	def test_ne_value(self):
		assert self.item != 99
		assert 99 != self.item

	def test_ne_item(self):
		assert self.item != Item(99)

	def test_str(self):
		assert str(self.item) == "100"

	def test_int(self):
		assert int(self.item) == 100
		assert isinstance(int(self.item), int)

	def test_float(self):
		assert float(self.item) == 100.0
		assert isinstance(float(self.item), float)
