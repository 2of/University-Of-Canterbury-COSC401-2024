from math import exp
import numpy as np



def one_hot_encoding(ys):
    num_rows = len(ys)
    if (num_rows == 0):
        return []
    num_cols = max(ys) + 1

    encoding = np.zeros((num_rows, num_cols), dtype=int)
    
    for i,y in enumerate(ys):
        encoding[i][y] = 1
    return encoding

def softmax(z):
    # had to add just in case z is of wrong shape :/
    if len(z.shape) == 1:
        z = z.reshape(1, -1)
    exp_scores = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)


def softmax_regression(xs, ys, learning_rate, num_iterations):
    n, m = xs.shape  # n: number of examples, m: number of features
    xs = np.concatenate([xs, np.ones((n, 1))], axis=1)
    #old issue was
    #xs_with_bias = np.column_stack((np.ones(n), xs))
    # Above puts them the wrong way a-bloody-round
    #
    theta = np.zeros((max(ys) + 1, xs.shape[1]))
    t = one_hot_encoding(ys)
    
    for _ in range(num_iterations):
        z = np.dot(xs, theta.T) #grad decent
        o = softmax(z)
        grad_J = np.dot((o - t).T, xs)
        theta -= learning_rate * grad_J
    
    def h(x):
        x = np.append(x, 1) ## bias again
        z = np.dot(theta, x)
        o = softmax(z)
        return np.argmax(o) #highest prob at i
    
    return h


training_data = np.array([
    (0.17, 0),
    (0.79, 0),
    (2.66, 2),
    (2.81, 2),
    (1.58, 1),
    (1.86, 1),
    (2.97, 2),
    (2.70, 2),
    (1.64, 1),
    (1.68, 1)
])

xs = training_data[:, 0].reshape((-1, 1))  # a 2D n-by-1 array
ys = training_data[:, 1].astype(int)      # a 1D array of length n

h = softmax_regression(xs, ys, 0.05, 750)

test_inputs = [(1.30, 1), (2.25, 2), (0.97, 0), (1.07, 1), (1.51, 1)]
print(f"{'prediction':^10}{'true':^10}")
for x, y in test_inputs:
    print(f"{h(x):^10}{y:^10}")
