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
        print(test, test.T)
        test = test.reshape(-1, 1)
        print(test)
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