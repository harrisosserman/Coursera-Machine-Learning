import matplotlib.pyplot as plt
import numpy
import math

ALPHA = .01

coordinates = []
with open('ex2data1.txt') as inputfile:
	for line in inputfile:
		coordinate = line.strip().split(',')
		# print coordinates
		coordinates.append([float(coordinate[0]), float(coordinate[1]), float(coordinate[2])])


def sigmoid(input):
	return (1/(1 + math.exp(-1 * input)))

def gradient(theta_transpose_times_x, x, output):
	return (sigmoid(theta_transpose_times_x) - output) * x

theta_0 = 0
theta_1 = 0
for iteration in range(0, 800):
	theta_0_derivative = 0.0
	theta_1_derivative = 0.0
	for index in range(len(coordinates)):
		theta_transpose_times_x = theta_0 * coordinates[index][0] + theta_1 * coordinates[index][1]
		theta_0_derivative += gradient(theta_transpose_times_x, coordinates[index][0], coordinates[index][2])
		theta_1_derivative += gradient(theta_transpose_times_x, coordinates[index][1], coordinates[index][2])
	print "theta_0_derivative", theta_0_derivative, "theta_1_derivative", theta_1_derivative
	theta_0 = theta_0 - ALPHA * (1.0 / len(coordinates)) * theta_0_derivative  
	theta_1 = theta_1 - ALPHA * (1.0 / len(coordinates)) * theta_1_derivative
	print "theta_0", theta_0, "theta_1", theta_1

def cost_function(theta, x, y):
	theta_transpose_times_x = theta[0] * x[0] + theta[1] * x[1]
	print "theta_transpose_times_x", theta_transpose_times_x
	return (-1.0) * y * math.log(sigmoid(theta_transpose_times_x)) - (1.0 - y) * math.log(sigmoid(1.0 - theta_transpose_times_x))

plt.scatter([cost_function([theta_0, theta_1], [x[0], x[1]], x[2]) for x in coordinates], [y_column[2] for y_column in coordinates])
plt.show()

