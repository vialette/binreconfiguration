"""Reconfigurable storage unit

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

import binreconfiguration.storageunit

class StorageUnit(binreconfiguration.storageunit.StorageUnit):

	def remove_item(self, bin_index, item):
		"""Remove an item in a bin of this storage unit.

	    :param bin_index: The index of the bin in this storage unit to remove an item from.
	    :type bin_index: int.
	    :param item: The item to be removes.
	    :type item: Item.

		"""
		self._bins[bin_index].remove_item(item)

	def move_item(self, source_bin_index, target_bin_index, item):
		"""Move an item from a bin to another in this storage unit.

	    :param source_bin_index: The index of the bin in this storage unit to remove an item from.
	    :type source_bin_index: int.
	    :param target_bin_index: The index of the bin in this storage unit to add an item in.
	    :type target_bin_index: int.
	    :param item: The item to be removes.
	    :type item: Item.

		"""
		if source_bin_index != target_bin_index:
			self.remove_item(source_bin_index, item)
			self.add_item(target_bin_index, item)