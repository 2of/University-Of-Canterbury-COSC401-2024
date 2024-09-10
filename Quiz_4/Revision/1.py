
def less_general_or_equal(ha, hb, X):
    # okay, this is the only way I can satisfy the h2 => h3 false and h3 => h2 false clause
    for x in X:
        if ha(x) > hb(x):
            return False
    return True


import numpy  as np

def linear_regression(xs, ys):
    #theta - (xTx)^-1 * xT*y
    # but add row of ones first

    x = np.hstack((np.ones((xs.shape[0], 1)), xs))
    print(x)
    a = np.dot(x.T, x)
    a = np.linalg.inv(a)
    a = np.dot(a,np.dot(x.T, ys))
    return a


	
import numpy as np

xs = np.arange(5).reshape((-1, 1))
ys = np.arange(1, 11, 2)
print(linear_regression(xs, ys))