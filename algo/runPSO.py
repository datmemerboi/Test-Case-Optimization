from PSO import PSO

def adder(arguments):
	# x1, x2, x3 = arguments
	return sum(arguments)


instance = PSO(func=adder, dim=3, lb=[1, 2, 3], ub=[10, 20, 30])
result = instance.run(max_iter=100)

print("Best values of x: ", result.gbest_x)
print("Best values of f(x): ",result.gbest_y)