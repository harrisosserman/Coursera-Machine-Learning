import scipy.io
import numpy
LAMBDA = 1.0
mat = scipy.io.loadmat('ex3data1.mat')
print "=====all keys: ", mat.keys()
# each row of X is an image with 20 different pixels and each row of y matches up to X.  
# when y[i] = 0, that means that the image is a 10, and 1-9 is 1-9...

def calculate_h(theta, x):
	theta_x = numpy.dot(numpy.matrix(x), numpy.matrix(theta))
	h = 1/(1 + numpy.exp(theta_x))
	return h

def unregularized_cost_function(theta, x, y):
	h = calculate_h(theta, x)
	log_h = numpy.log(h)
	log_1_minus_h = numpy.log(1 - h)
	summation = -1 * numpy.dot(numpy.transpose(y), log_h) - numpy.dot((1 - numpy.transpose(y)), log_1_minus_h)
	return (1.0 / len(y)) * summation[0][0]


def unregularized_gradient(theta, x, y):
	h = calculate_h(theta, x)
	h_minus_y = h - numpy.matrix(y)
	return (1.0 / len(y)) * numpy.dot(numpy.transpose(x), h_minus_y)

def regularized_gradient(theta, x, y):
	return unregularized_gradient(theta, x, y) + (LAMBDA / len(y)) * theta 


test_theta = numpy.ones((len(mat['X'][0]), 1))
print 'output of unregularized cost func: ', unregularized_cost_function(test_theta, mat['X'], mat['y'])
print 'output of unregularized gradient: ', unregularized_gradient(test_theta, mat['X'], mat['y'])
print 'output of regularized gradient: ', regularized_gradient(test_theta, mat['X'], mat['y'])