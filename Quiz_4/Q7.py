
import numpy as np
from math import exp
def monomial_kernel(d):
    #actually following the lecture notes this time
    def kernel(x,y):
        dp = np.dot(x,y)
        a =  (1+ sum([dp**i for i in range(1,d+1)]))
        return a
    return kernel



def rbf_kernel(sigma):
    def kernel(x,z):
        top = np.linalg.norm(x - z) ** 2
        bottom = 2 * (sigma **2)
        return exp(-1*(top/bottom))
    
    return kernel


sigmoid = lambda x: 1 / (1 + np.exp(-x))


def logistic_regression_with_k3ernel(xs, ys, k,alpha, iterations):
    # renamed to xs and ys for convienience :)
    n,m = xs.shape[0],xs.shape[1]

    thetaV = np.zeros(n)
   # kernels = np.zeros((n,n))
    # for i in range(n):
    #     for j in range(n):
    #         kernels[i,j] = k(xs[i], xs[j])
    # print(kernels)
    kernels = np.array([[k(xi, xj) for xj in xs] for xi in xs])
    for iteration in range(iterations):
        
        print(iteration)
        for i in range(n):
            yi = y[i]
            inner = np.dot(kernels[i], thetaV)
            print(inner, sigmoid(inner))
            h = sigmoid(np.dot(kernels[i], thetaV))
            gradient = (yi - h) * kernels[i]
            thetaV += alpha * gradient
            # print(thetaV)
            
            
            
    def model(x):
        kernel_x = np.array([k(x,xi) for xi in xs])
        return int(sigmoid(np.dot(kernel_x, thetaV)) > 0.5)
    return model


def logistic_regression_with_kernel(xs,s,k, alpha, iterations):
    n,m = xs.shape[0],xs.shape[1]

    thetaV = np.zeros()
    
    # compute ALL alues Ki xj
    kernels = np.array([[k(xi, xj) for xj in xs] for xi in xs])
    beta = np.zeros(n)
    print(beta)
    for n in range(iterations):
        pass
    
    
    
    
f = lambda x, y, z, w:  int(x*y*z - y**2*z*w/4 + x**4*w**3/8- y*w/2 >= 0)

training_examples = [
    ([0.254, 0.782, 0.254, 0.569], 0),
    ([0.237, 0.026, 0.237, 0.638], 0),
    ([0.814, 0.18, 0.814, 0.707], 1),
    ([0.855, 0.117, 0.855, 0.669], 1),
    ([0.776, 0.643, 0.776, 0.628], 1),
    ([0.701, 0.71, 0.701, 0.982], 0),
    ([0.443, 0.039, 0.443, 0.356], 1),
    ([0.278, 0.105, 0.278, 0.158], 0),
    ([0.394, 0.203, 0.394, 0.909], 0),
    ([0.83, 0.197, 0.83, 0.779], 1),
    ([0.277, 0.415, 0.277, 0.357], 0),
    ([0.683, 0.117, 0.683, 0.455], 1),
    ([0.421, 0.631, 0.421, 0.015], 1)
]

X, y = map(np.array, zip(*training_examples))

h = logistic_regression_with_kernel(X, y, monomial_kernel(10), 0.01, 500)

test_examples = [
    ([0.157, 0.715, 0.787, 0.644], 0),
    ([0.79, 0.279, 0.761, 0.886], 1),
    ([0.903, 0.544, 0.138, 0.925], 0),
    ([0.129, 0.01, 0.493, 0.658], 0),
    ([0.673, 0.526, 0.672, 0.489], 1),
    ([0.703, 0.716, 0.088, 0.674], 0),
    ([0.276, 0.174, 0.69, 0.358], 1),
    ([0.199, 0.812, 0.825, 0.653], 0),
    ([0.332, 0.721, 0.148, 0.541], 0),
    ([0.51, 0.956, 0.023, 0.249], 0)
]
print(f"{'x' : ^30}{'prediction' : ^11}{'true' : ^6}")
for x, y in test_examples:
    print(f"{str(x) : ^30}{int(h(np.array(x))) : ^11}{y : ^6}")