import numpy as np
def logistic_regression(xs, ys, alpha, num_iterations):
    # Implement stochastic gradient descent
    sigmoid = lambda x: 1 / (1 + np.exp(-x))
    ones = np.ones((xs.shape[0], 1))
    xs = np.hstack((ones, xs))
    
    theta = np.zeros(xs.shape[1])
    
    for _ in range(num_iterations):
        for i in range(xs.shape[0]):
            prediction = sigmoid(np.dot(xs[i], theta))
            error = ys[i] - prediction
            gradient = error * xs[i]
            theta += alpha * gradient
    print(theta)
    
    
    def model(new_xs):
        new_xs = np.insert(new_xs,0,1)
        return sigmoid(np.dot(new_xs,theta))
    return model


import numpy as np

# The input has one dimension.

# Training data:
xs = np.array([1, 2, 3, 101, 102, 103]).reshape((-1, 1)) # an n-by-1 matrix of inputs
ys = np.array([0, 0, 0, 1, 1, 1]) # n-element vector of outputs

# Fitting a model
model = logistic_regression(xs, ys, 0.05, 10000)

test_inputs = np.array([1.5, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101.8, 97]).reshape((-1, 1))

for test_input in test_inputs:
    print("{:.2f}".format(np.array(model(test_input)).item()))