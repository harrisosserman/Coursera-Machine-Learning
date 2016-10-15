import scipy.io
import numpy
mat = scipy.io.loadmat('ex3data1.mat')
print mat
print "=====all keys: ", mat.keys()
# each row of X is an image with 20 different pixels and each row of y matches up to X.  
# when y[i] = 0, that means that the image is a 10, and 1-9 is 1-9...

def unregularized_cost_function(theta, x, y):
	# theta is assumed to be a vertical vector
	theta_x = numpy.matrix(x) * numpy.matrix(theta)
	log_h = numpy.log(1/(1 + numpy.exp(theta_x)))

	# ouptut = -1 * numpy.matrix(y)


test_theta = numpy.ones(len(mat['y']), 1)
unregularized_cost_function(test_theta, mat['X'], mat['y'])