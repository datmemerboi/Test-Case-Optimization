from PSO import PSO

def fitness_fn(arguments):
	x1, x2, x3, x4, x5 = arguments

	if x2==x3:
		x3 = 0
	if x1 == x2 or x1 == x3:
		x2 = x3 = 0
	if x3 > x1 and x3 > x2:
		x1 = x2 = 0
	if x2 > x1 and x2 > x3:
		x1 = x3 = 0
	if x1 > x2 and x1 > x3:
		x2 = x3 = 0

	return (x1*0.9 + x2*0.5 + x3*0.1)*x4*x5

instance = PSO(
	func=fitness_fn, dim=3,
	lb=[0, 0, 0, 1, 1],
	ub=[2, 2, 2, 20, 20]
	)
result = instance.run(max_iter=100)

print("Best values of x: ", result.gbest_x)
print("Best values of f(x): ",result.gbest_y)