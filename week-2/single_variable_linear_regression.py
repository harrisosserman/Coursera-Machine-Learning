ALPHA = 0.023

coordinates = []
with open('ex1data1.txt') as inputfile:
	for line in inputfile:
		coordinate = line.strip().split(',')
		# print coordinates
		coordinates.append([float(coordinate[0]), float(coordinate[1])])


theta_0 = 0
theta_1 = 0

def h_function(x):
	return theta_0 + x*theta_1

def cost_function(x, y):
	return h_function(x) - y 

for iteration in range(0, 8000):
	total_error_theta_0 = 0
	total_error_theta_1 = 0
	for index in range(0, len(coordinates)):
		total_error_theta_0 += cost_function(coordinates[index][0], coordinates[index][1])
		total_error_theta_1 += cost_function(coordinates[index][0], coordinates[index][1]) * coordinates[index][0]
	print total_error_theta_0
	print total_error_theta_1
	theta_0 = theta_0 - ALPHA * 1 / len(coordinates) * total_error_theta_0
	theta_1 = theta_1 - ALPHA * 1 / len(coordinates) * total_error_theta_1

print "THETA_0", theta_0, "THETA_1", theta_1