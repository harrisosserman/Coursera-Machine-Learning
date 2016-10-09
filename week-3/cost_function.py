import matplotlib.pyplot as plt
import numpy
import math

ALPHA = .0005

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

gradient_0 = []
gradient_1 = []

theta_0 = 0
theta_1 = 0
for iteration in range(0, 5000):
	theta_0_derivative = 0.0
	theta_1_derivative = 0.0
	for index in range(len(coordinates)):
		theta_transpose_times_x = theta_0 * coordinates[index][0] + theta_1 * coordinates[index][1]
		theta_0_derivative += gradient(theta_transpose_times_x, coordinates[index][0], coordinates[index][2])
		theta_1_derivative += gradient(theta_transpose_times_x, coordinates[index][1], coordinates[index][2])
	gradient_0.append(ALPHA * (1.0 / len(coordinates)) * theta_0_derivative)
	gradient_1.append(ALPHA * (1.0 / len(coordinates)) * theta_1_derivative )
	theta_0 = theta_0 - ALPHA * (1.0 / len(coordinates)) * theta_0_derivative  
	theta_1 = theta_1 - ALPHA * (1.0 / len(coordinates)) * theta_1_derivative
	print "theta_0", theta_0, "theta_1", theta_1

def cost_function(theta, x, y):
	theta_transpose_times_x = theta[0] * x[0] + theta[1] * x[1]
	return (-1.0) * y * math.log(sigmoid(theta_transpose_times_x)) - (1.0 - y) * math.log(sigmoid(1.0 - theta_transpose_times_x))



print "admission probability (should be 0.776): ", sigmoid(theta_0 * 45.0 + theta_1 * 85.0)

# plots of gradient descent error
# plt.figure(1)
# plt.scatter(range(0, 5000), gradient_0)

# plt.figure(2)
# plt.scatter(range(0, 5000), gradient_1)
# plt.show()

# admitted_training_set = filter(lambda row:sigmoid(row[0] * theta_0 + row[1] * theta_1) > 0.5, coordinates)
# not_admitted_training_set = filter(lambda row:sigmoid(row[0] * theta_0 + row[1] * theta_1) <= 0.5, coordinates)

admitted_training_set = filter(lambda row:row[2] == 1, coordinates)
not_admitted_training_set = filter(lambda row:row[2] == 0, coordinates)

plt.scatter([exam_1[0] for exam_1 in admitted_training_set], [exam_2[1] for exam_2 in admitted_training_set], marker="o")
plt.scatter([exam_1[0] for exam_1 in not_admitted_training_set], [exam_2[1] for exam_2 in not_admitted_training_set], marker="x")
plt.show()

