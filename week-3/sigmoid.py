import matplotlib.pyplot as plt
import numpy
import math

coordinates = []
with open('ex2data1.txt') as inputfile:
	for line in inputfile:
		coordinate = line.strip().split(',')
		# print coordinates
		coordinates.append([float(coordinate[0]), float(coordinate[1])])


def sigmoid(input):
	return (1/(1 + math.exp(-1 * input)))

plt.figure(2)
x_data_points = numpy.linspace(0, 20, 1000)
y_data_points = [sigmoid(x_data_point) for x_data_point in x_data_points]
plt.plot(x_data_points, y_data_points)
plt.show()