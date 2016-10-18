import scipy.io
import scipy.optimize
import numpy
mat = scipy.io.loadmat('ex3data1.mat')
print "=====all keys: ", mat.keys()
# each row of X is an image with 20 different pixels and each row of y matches up to X.  
# when y[i] = 0, that means that the image is a 10, and 1-9 is 1-9...

def calculate_h(theta, x):
	print 'x shape: ', numpy.matrix(x).shape
	print 'theta shape: ', numpy.matrix(theta).shape
	theta_x = numpy.dot(x, theta)
	print 'theta_x shape: ', theta_x.shape
	h = 1/(1 + numpy.exp(theta_x))
	return h

def unregularized_cost_function(theta, x, y):
	# TODO: make a regularized cost function to pass into optimizing func
	h = calculate_h(theta, x)
	log_h = numpy.log(h)
	log_1_minus_h = numpy.log(1 - h)
	print 'y shape: ', y.shape
	print 'log_h_shape ', log_h.shape
	print 'log_1_minus', log_1_minus_h.shape
	summation = -1 * numpy.dot(numpy.transpose(y), log_h) - numpy.dot((1 - numpy.transpose(y)), log_1_minus_h)
	print 'summation; ', summation
	return (1.0 / len(y)) * summation


def unregularized_gradient(theta, x, y):
	h = calculate_h(theta, x)
	h_minus_y = h - numpy.matrix(y)
	return (1.0 / len(y)) * numpy.dot(numpy.transpose(x), h_minus_y)

def regularized_gradient(theta, x, y):
	# use a lambda of 0.1
	return unregularized_gradient(theta, x, y) + (0.1 / len(y)) * numpy.transpose(theta) 

def regularized_gradient_helper(theta, *args):
	return regularized_gradient(theta, args[0], args[1])

def regularized_cost_helper(theta, *args):
	return unregularized_cost_function(theta, args[0], args[1])


initial_theta = numpy.ones((len(mat['X'][0]), 1))
print 'initial theta shape: ', initial_theta.shape
# print 'output of unregularized cost func: ', unregularized_cost_function(initial_theta, mat['X'], mat['y'])
# print 'output of unregularized gradient: ', unregularized_gradient(initial_theta, mat['X'], mat['y'])
# print 'output of regularized gradient: ', regularized_gradient(initial_theta, mat['X'], mat['y'])

# iteration maps to the digit that we are building a classifier for (1-10)
for iteration in range(1, 10):
	y_vector = numpy.transpose(map(lambda row:1 if ((row[0] % iteration == 0 or (row[0] == 0 and iteration == 10))) else 0, mat['y']))
	response = scipy.optimize.fmin_cg(regularized_cost_helper, initial_theta, regularized_cost_helper, args=(mat['X'], y_vector))
	print response
