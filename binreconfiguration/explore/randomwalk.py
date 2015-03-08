from .explore import Explore
from binreconfiguration.storageunit import StorageException
import random

class RandomWalk(Explore):

	def step(self):
		source_bins = self._storage_unit.non_empty_bins()
		random.shuffle(source_bins)
		for source_bin in source_bins:
			items = [item for item in source_bin]
			random.shuffle(items)

			for item in items:
				target_bins = [target_bin 
							   for target_bin in self._storage_unit.bins_with_freespace(item)
							   if target_bin != source_bin]
				if target_bins != []:
					target_bin = random.choice(target_bins)
					self._storage_unit.move(item, source_bin, target_bin)
					return True

		return False


	def run(self, fun):
		self._number_of_steps = 0
		while not fun(self):
			if self.step():
				self._number_of_steps += 1
			else:
				raise ExploreException()

