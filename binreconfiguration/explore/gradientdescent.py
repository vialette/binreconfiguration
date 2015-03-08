from .explore import Explore
from binreconfiguration.storageunit import StorageException
import random

class GradientDescent(Explore):

	def step(self):
		best_move_so_far    = None
		best_fitness_so_far = None

		# for each non-empty source bin
		source_bins = self.storage_unit().non_empty_bins()
		for source_bin in source_bins:

			# for every item in the source bin
			items = [item for item in source_bin]
			for item in items:
				
				# for every large enough target bin
				target_bins = [target_bin 
							   for target_bin in self.storage_unit().bins_with_freespace(item)
							   if target_bin != source_bin]
				for target_bin in target_bins:
					# compute the hypothetical fitness and keep the best one
					fitness = self._fitness_fun(self.....)
					if best_fitness_so_far is None or fitness > best_fitness_so_far:
						best_fitness_so_far = fitness
						best_move_so_far = (item, source_bin, target_bin)

		if best_fitness_so_far is not None:
			(item, source_bin, target_bin) = best_move_so_far
			self.storage_unit().move(item, source_bin, target_bin)
			return True
		else:
			# no move is possible, i.e. local optimum
			return False


	def run(self, fitness_fun):
		self._number_of_steps = 0
		self._fitness = fitness_fun(self.storage_unit())
		self._fitness_fun = fitness_fun
		while not fun(self):
			if self.step():
				self._number_of_steps += 1
			else:
				raise ExploreException()
		self._fitness_fun = None
