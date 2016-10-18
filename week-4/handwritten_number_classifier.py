import scipy.io
import scipy.optimize
import numpy
mat = scipy.io.loadmat('ex3data1.mat')
print "=====all keys: ", mat.keys()
# each row of X is an image with 20 different pixels and each row of y matches up to X.  
# when y[i] = 0, that means that the image is a 10, and 1-9 is 1-9...

def calculate_h(theta, x):
	theta_x = numpy.dot(x, theta)
	h = 1.0/(1.0 + numpy.exp(theta_x))
	return h

def unregularized_cost_function(theta, x, y):
	h = calculate_h(theta, x)
	log_h = numpy.log(h)
	log_1_minus_h = numpy.log(1.0 - h)
	summation_of_unregularized_cost = -1.0 * numpy.dot(numpy.transpose(y), log_h) - numpy.dot((1.0 - numpy.transpose(y)), log_1_minus_h)
	summation_of_unregularized_cost = (1.0 / len(y)) * summation_of_unregularized_cost
	return summation_of_unregularized_cost

def regularized_cost_function(theta, x, y):
	summation_of_unregularized_cost = unregularized_cost_function(theta, x, y)
	regularization_term = (0.1 / (2.0 * len(y))) * numpy.sum(numpy.power(theta, 2))
	print 'regularize cost func output', summation_of_unregularized_cost + regularization_term
	return summation_of_unregularized_cost + regularization_term

def unregularized_gradient(theta, x, y):
	h = calculate_h(theta, x)
	h_minus_y = h - numpy.matrix(y)
	return (1.0 / len(y)) * numpy.dot(h_minus_y, x)

def regularized_gradient(theta, x, y):
	# use a lambda of 0.1
	print 'regularized gradient output shape: ', numpy.matrix(unregularized_gradient(theta, x, y) + (0.1 / len(y)) * numpy.transpose(theta)).shape 
	return unregularized_gradient(theta, x, y) + (0.1 / len(y)) * numpy.transpose(theta) 

def regularized_gradient_helper(theta, *args):
	print 'in gradient helper, sizes are: ', theta.shape, args[0].shape, args[1].shape
	return regularized_gradient(theta, args[0], args[1])

def regularized_cost_helper(theta, *args):
	print 'in cost helper, sizes are: ', theta.shape, args[0].shape, args[1].shape
	return regularized_cost_function(theta, args[0], args[1])

initial_theta = numpy.random.rand(1, len(mat['X'][0]))
# print 'output of unregularized cost func: ', unregularized_cost_function(initial_theta, mat['X'], mat['y'])
# print 'output of unregularized gradient: ', unregularized_gradient(initial_theta, mat['X'], mat['y'])
# print 'output of regularized gradient: ', regularized_gradient(initial_theta, mat['X'], mat['y'])

# iteration maps to the digit that we are building a classifier for (1-10)
for iteration in range(1, 10):
	y_vector = numpy.transpose(map(lambda row:1 if ((row[0] % iteration == 0 or (row[0] == 0 and iteration == 10))) else 0, mat['y']))
	response = scipy.optimize.fmin_cg(regularized_cost_helper, initial_theta, regularized_gradient_helper, args=(mat['X'], y_vector))
	print response
