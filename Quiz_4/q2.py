import numpy as np

def linear_regression(xs,ys,basis_functions=None, penalty = 0): 
    if basis_functions == None:
        x = np.hstack((np.ones((xs.shape[0],1)),xs))
        #print(x)
    else:
        #as q1 ? 
        k = np.ones((xs.shape[0],1))
        
        for func in basis_functions:
                    test = np.array([func(a) for a in xs])
                    test = test.reshape(-1, 1)
                    k = np.hstack((k, test))
        x = k
    xtx = np.dot(x.T,x)
    
    
    
    if penalty == 0:
        
        xtx_inv = np.linalg.inv(xtx)
        xty = np.dot(x.T, ys)
        a = np.dot(xtx_inv, xty)
        
    else:
        penalties_id_matrix = np.eye(x.shape[1])
        penalties_id_matrix = penalty * penalties_id_matrix
        
        
        xtxp = xtx + penalties_id_matrix
        xtxpinv = np.linalg.inv(xtxp)
        xty = np.dot(x.T, ys)
        a = np.dot(xtxpinv, xty)
    return a



import numpy as np

xs = np.arange(5).reshape((-1, 1))
ys = np.arange(1, 11, 2)

print(linear_regression(xs, ys), end="\n\n")

with np.printoptions(precision=5, suppress=True):
    print(linear_regression(xs, ys, penalty=0.1))
    
    
    
import numpy as np

# we set the seed to some number so we can replicate the computation
np.random.seed(0)

xs = np.arange(-1, 1, 0.1).reshape(-1, 1)
m, n = xs.shape
# Some true function plus some noise:
ys = (xs**2 - 3*xs + 2 + np.random.normal(0, 0.5, (m, 1))).ravel()

functions = [lambda x: x[0], lambda x: x[0]**2, lambda x: x[0]**3, lambda x: x[0]**4,
      lambda x: x[0]**5, lambda x: x[0]**6, lambda x: x[0]**7, lambda x: x[0]**8]

for penalty in [0, 0.01, 0.1, 1, 10]:
    with np.printoptions(precision=5, suppress=True):
        print(linear_regression(xs, ys, basis_functions=functions, penalty=penalty)
              .reshape((-1, 1)), end="\n\n")

