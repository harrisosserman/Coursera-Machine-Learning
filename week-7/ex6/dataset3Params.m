function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

lowest_prediction_error = -1
lowest_C = 1;
lowest_sigma = 0.3;
values_of_c_and_sigma = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
for c_index = 1:length(values_of_c_and_sigma)
  for sigma_index = 1:length(values_of_c_and_sigma)
    C = values_of_c_and_sigma(c_index);
    sigma = values_of_c_and_sigma(sigma_index);
    disp("model is");
    model= svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));
    predictions = svmPredict(model, Xval);
    prediction_error = mean(double(predictions ~= yval))
    if (lowest_prediction_error == -1 || prediction_error < lowest_prediction_error)
      lowest_prediction_error = prediction_error;
      lowest_C = C;
      lowest_sigma = sigma;
    endif
  endfor
endfor

C = lowest_C;
sigma = lowest_sigma;


% =========================================================================

end
