import scipy.io
import numpy
mat = scipy.io.loadmat('ex3data1.mat')
print "=====all keys: ", mat.keys()
# each row of X is an image with 20 different pixels and each row of y matches up to X.  
# when y[i] = 0, that means that the image is a 10, and 1-9 is 1-9...

def unregularized_cost_function(theta, x, y):
	# theta is assumed to be a vertical vector
	theta_x = numpy.matrix(x) * numpy.matrix(theta)
	h = 1/(1 + numpy.exp(theta_x))
	log_h = numpy.log(h)
	log_1_minus_h = numpy.log(1 - h)
	# TODO: look into why you need to do the dot product
	summation = -1 * numpy.dot(numpy.transpose(y), log_h) - numpy.dot((1 - numpy.transpose(y)), log_1_minus_h)
	return (1.0 / len(y)) * summation[0][0]


test_theta = numpy.ones((len(mat['X'][0]), 1))
print 'output of func: ', unregularized_cost_function(test_theta, mat['X'], mat['y'])