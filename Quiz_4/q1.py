import numpy  as np



def linear_regression(xs, ys, functions=None):
    # so if the list is empty, we good, if functions is none we match the other cases, I think this must be alright?
    if functions == None:
        x = np.hstack((np.ones((xs.shape[0], 1)), xs))
        a = np.dot(x.T,x)
        a = np.linalg.inv(a)
        a = np.dot(a, np.dot(x.T, ys))
        return a

    k = np.ones((xs.shape[0], 1))
    for func in functions:
        test = np.array([func(a) for a in xs])
        test = test.reshape(-1, 1)
        k = np.hstack((k, test))
    x = k
    a = np.dot(x.T,x)
    a = np.linalg.inv(a)
    a = np.dot(a, np.dot(x.T, ys))
    return a




import numpy as np

xs = np.arange(5).reshape((-1, 1))
ys = np.array([3, 6, 11, 18, 27])
# Can you see y as a function of x? [hint: it's quadratic.]
functions = [lambda x: x[0], lambda x: x[0] ** 2]
print(linear_regression(xs, ys, functions))


import numpy as np

xs = np.array([[1, 2, 3, 4],
               [6, 2, 9, 1]]).T
ys = np.array([7, 5, 14, 8])

# print(linear_regression(xs,ys,[]))
# print(np.average(ys))
print(linear_regression(xs, ys, []) == np.average(ys))




import numpy as np

xs = np.arange(5).reshape((-1, 1))
ys = np.array([-3.95, -3.9, 2.2, 20.4, 56.8])
functions = [lambda x: x[0], lambda x: x[0]**2, lambda x: x[0]**3, lambda x: 2**x[0]]
coefficients = linear_regression(xs, ys, functions).ravel()
expected = np.array([-4.000, -1.000, 0.000, 1.000, 0.050])
if np.allclose(coefficients, expected):
    print("OK")
else:
    print("The following returned coefficients\n are not close to the expected answer.")
    print(coefficients)


    print("{:.3f}".format(coefficient))
    
    
	
import numpy as np

xs = np.arange(5).reshape((-1, 1))
ys = np.arange(1, 11, 2)
print(linear_regression(xs, ys))


import numpy as np

xs = np.array([[1, 2, 3, 4],
               [6, 2, 9, 1]]).T
ys = np.array([7, 5, 14, 8]).T
print(linear_regression(xs, ys))