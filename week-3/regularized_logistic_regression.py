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

for iteration in range(0, 15000):
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


plt.scatter([exam_1[0] for exam_1 in predict_yes], [exam_2[1] for exam_2 in predict_yes], marker="o")
plt.scatter([exam_1[0] for exam_1 in predict_no], [exam_2[1] for exam_2 in predict_no], marker="x")
plt.show()

