from .gradientdescent import GradientDescent

class MinGradientDescent(GradientDescent):
	
	@abc.abstractmethod
	def cmp_fitness(fitness, best_fitness):
		return fitness < best_fitness