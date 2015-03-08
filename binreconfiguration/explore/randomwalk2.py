from .explore import Explore
from binreconfiguration.storageunit import StorageException
import random

class RandomWalk(Explore):

	def step(self):
		item_bin_pairs = [(bin, item) for bin i self._storage_unit for item in bin]
		random.shuffle(item_bin_pairs)
		for (item, source_bin) in item_bin_pairs:
			target_bins = [target_bin 
						   for btarget_in in self._storage_unit.bins_with_freespace(item)
						   if target_bin != source_bin]
			if target_bins != []:
				target_bin = random.choice(target_bins)
				self._storage_unit.move(item, source_bin, target_bin)
				return True

		# still here!? no move is posible.
		return False


	def run(self, fun):
		self._number_of_steps = 0
		while not fun(self):
			if self.step():
				self._number_of_steps += 1
			else:
				raise ExploreException()

