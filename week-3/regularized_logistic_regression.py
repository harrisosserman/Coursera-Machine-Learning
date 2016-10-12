import matplotlib.pyplot as plt
import numpy
import math
from sklearn.preprocessing import PolynomialFeatures

ALPHA = .05
LAMBDA = 1

coordinates = []
with open('ex2data2.txt') as inputfile:
	for line in inputfile:
		coordinate = line.strip().split(',')
		# print coordinates
		coordinates.append([float(coordinate[0]), float(coordinate[1]), float(coordinate[2])])


def sigmoid(input):
	return (1/(1 + math.exp(-1 * input)))

poly = PolynomialFeatures(degree=6)
polynomial_features = poly.fit_transform(map(lambda row:[row[0], row[1]], coordinates))

theta = numpy.ones(len(polynomial_features[0]))

for iteration in range(0, 1500):
	theta_derivatives = numpy.zeros(len(polynomial_features[0]))
	for index in range(len(coordinates)):
		prediction_for_row = (sigmoid(numpy.dot(polynomial_features[index], theta)) - coordinates[index][2])
		for feature in range(len(polynomial_features[0])):
			theta_derivatives[feature] += prediction_for_row * polynomial_features[index][feature]
	for feature in range(len(polynomial_features[0])):
		if feature == 0:
			theta_derivatives[feature] = (1.0 / len(coordinates)) * theta_derivatives[feature]
		else:
			theta_derivatives[feature] = (1.0 / len(coordinates)) * theta_derivatives[feature] + (LAMBDA / len(coordinates)) * theta[feature]
		theta[feature] = theta[feature] - ALPHA * theta_derivatives[feature]
print theta

predict_yes = []
predict_no = []
for index in range(len(coordinates)):
	if (sigmoid(numpy.dot(theta, polynomial_features[index])) > 0.5):
		predict_yes.append(coordinates[index])
	else:
		predict_no.append(coordinates[index])


plt.figure(1)
plt.scatter([exam_1[0] for exam_1 in predict_yes], [exam_2[1] for exam_2 in predict_yes], marker="o")
plt.scatter([exam_1[0] for exam_1 in predict_no], [exam_2[1] for exam_2 in predict_no], marker="x")


# find the place where theta * x == 0
x1_data_points = numpy.linspace(-1, 1, 100)
x2_data_points = numpy.linspace(-1, 1, 100)
data_points = []
for x1_index in range(0, 100):
	for x2_index in range(0, 100):
		data_points.append([x1_data_points[x1_index], x2_data_points[x2_index]])
poly = PolynomialFeatures(degree=6)
polynomial_features = poly.fit_transform(map(lambda row:[row[0], row[1]], data_points))
predict_yes = []
predict_no = []
for index in range(len(polynomial_features)):
	if (sigmoid(numpy.dot(theta, polynomial_features[index])) > 0.5):
		predict_yes.append(data_points[index])
	else:
		predict_no.append(data_points[index])

plt.figure(2)
plt.scatter([exam_1[0] for exam_1 in predict_no], [exam_2[1] for exam_2 in predict_no], marker="x")
plt.show()

