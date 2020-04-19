from GA import GeneticAlgorithm

# Fn to be used by the algorithm
def fitness_function(genome):
	x1, x2, x3, x4, x5 = genome
	return x1*0.9 + x2*0.5 + x3*0.1 +  (1-( x4/x5 ) )

# Size of Population used in algorithm
population_size = 100

# Number of arugment returned from fitness_function
genome_length = 5

ga = GeneticAlgorithm(
	fitness_function, 
	pop_size=population_size, 
	genome_length=genome_length,
	lb=[0, 0, 0, 10, 10],
	ub=[2, 2, 2, 20, 20]
)
ga.generate_binary_population()

# No. of pairs of individuals to be picked to mate
ga.number_of_pairs = 4

# Selective pressure from interval [1.0, 2.0]
# the lower value, the less will the fitness play role

# ga.selective_pressure = 1.5
# ga.mutation_rate = 0.1

# Mention number of iterations to run algorithm
ga.run(1000)

best_genome, best_fitness = ga.get_best_genome()
print("Best values for x: ", (1*best_genome))
print("Best value for f(x):", best_fitness)

# population = ga.population
# print(population, " population")

# fitness_vector = ga.get_fitness_vector()
# print(fitness_vector, " fit vec")