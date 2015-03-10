"""Storage unit context manager"""

class M(object):
	def __init__(self, storage_unit, item, source_bin_index, target_bin_index):
		self._storage_unit     = storage_unit
		self._item             = item
		self._source_bin_index = source_bin_index
		self._target_bin_index = target_bin_index

	def __enter__(self):
		self._storage_unit.move_item(self._source_bin_index, self._target_bin_index, self._item)

	def __exit__(self):
		self._storage_unit.move_item(self._target_bin_index, self._source_bin_index, self._item)