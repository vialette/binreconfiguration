from binreconfiguration import Bin
from binreconfiguration import Item
import re

class TestBin_Empty(object):

	def setup(self):
		self.capacity = 100
		self.bin = Bin(self.capacity)

	def test_capacity(self):
		assert self.bin.capacity() == self.capacity

	def test_count(self):
		assert self.bin.count() == 0

	def test_size(self):
		assert self.bin.size() == 0

	def test_free_space(self):
		assert self.bin.free_space() == self.capacity

	def test_load(self):
		assert self.bin.load() == 0

	def test_is_empty(self):
		assert self.bin.is_empty()

class TestBin_Name(object):
	def test_no_name(self):
		bin = Bin(10)
		pattern = re.compile('^Bin-(\d)+$')
		assert pattern.match(bin.name())

	def test_name(self):
		bin = Bin(10, "my bin")
		assert bin.name() == "my bin"

class TestBin_InsertOne(object):
	def setup(self):
		self.capacity  = 10
		self.item_size = 1
		self.bin  = Bin(self.capacity)
		self.item = Item(self.item_size)
		self.bin.add_item(self.item)

	def test_capacity(self):
		assert self.bin.capacity() == self.capacity

	def test_count(self):
		assert self.bin.count() == 1

	def test_size(self):
		assert self.bin.size() == self.item_size

	def test_free_space(self):
		assert self.bin.free_space() == self.capacity - self.item_size

	def test_load(self):
		assert self.bin.load() == float(self.item_size) / self.capacity

	def test_isempty(self):
		assert not self.bin.is_empty()

class TestBin_InsertMany(object):
	def setup(self):
		self.capacity = 10
		self.bin      = Bin(self.capacity)
		self.items    = [Item(i) for i in range(1,5)]
		for item in self.items:
			self.bin.add_item(item)

	def test_capacity(self):
		assert self.bin.capacity() == self.capacity

	def test_count(self):
		assert self.bin.count() == len(self.items)

	def test_size(self):
		assert self.bin.size() == sum(self.items)

	def test_free_space(self):
		assert self.bin.free_space() == self.capacity - sum(self.items)

	def test_load(self):
		assert self.bin.load() == float(sum(self.items)) / self.capacity

	def test_isempty(self):
		assert not self.bin.is_empty()

class TestBin_Snapshot(self):
	def setup(self):
		self.capacity = 10
		self.bin      = Bin(self.capacity)
		self.items    = [Item(i) for i in range(1,5)]
