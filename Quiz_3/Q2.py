def linear_regression(xs, ys):
    #theta - (xTx)^-1 * xT*y
    # but add row of ones first

    x = np.hstack((np.ones((xs.shape[0], 1)), xs))
    a = np.dot(x.T, x)
    a = np.linalg.inv(a)
    a = np.dot(a,np.dot(x.T, ys))
    return a

    # Compute the normal equation using dot product
    xs_transpose = xs_with_intercept.T
    theta = np.dot(np.dot(np.linalg.inv(np.dot(xs_transpose, xs_with_intercept)), xs_transpose), ys)

    return theta



def linear_regression2(xs, ys):
    first_col_ones = np.ones((xs.shape[0],1))

import numpy as np

xs = np.arange(5).reshape((-1, 1))
ys = np.arange(1, 11, 2)
print(linear_regression(xs, ys))



import numpy as np

xs = np.array([[1, 2, 3, 4],
               [6, 2, 9, 1]]).T
ys = np.array([7, 5, 14, 8]).T
print(linear_regression(xs, ys))