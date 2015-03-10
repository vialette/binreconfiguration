"""Minimum gradient descent.

.. moduleauthor:: Stéphane Vialette <vialette@gmail.com>

"""

from .gradientdescent import GradientDescent

class MinGradientDescent(GradientDescent):
	
	@abc.abstractmethod
	def cmp_fitness(fitness, best_fitness):
		"""

	    :param fitness: The fitness function.
	    :type fitness: function.
	    :param best_fitness: The fitness seen so far.
	    :type best_fitness: numeric.

		"""
		return fitness < best_fitness