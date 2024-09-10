import numpy as np
def monomial_kernel(d):
    #actually following the lecture notes this time
    
    
    def kernel(x,y):
        dp = np.dot(x,y)
        a =  (1+ sum([dp**i for i in range(1,d+1)]))
        return a
    return kernel
# The monomial kernel of order 1 is just fitting a bias
k = monomial_kernel(1)
x = np.array([1])
y = np.array([2])
print(k(x, y) == 1 + (x * y).item())

	
import numpy as np
# The feature map in the question example
phi = lambda z: [1, z[0], z[1], z[0]*z[1], z[1]*z[0], z[0]**2, z[1]**2]
k = monomial_kernel(2)
x = np.array([1, 2])
y = np.array([3, 0.5])
print(k(x, y) == np.dot(phi(x), phi(y)))


	
import itertools
import math
import numpy as np

d = 10
k = monomial_kernel(d)
def phi(z): # Probably a nicer way to do this...
    features = range(len(z))
    mapped = []
    for bits in range(d + 1):
        for indices in itertools.product(features, repeat=bits):
            mapped.append(math.prod(z[j] for j in indices))
    return mapped

x = np.array([0.15, -0.6, 7.1])
y = np.array([-3.1, 0.01, -0.24])
print(np.isclose(k(x, y), np.dot(phi(x), phi(y))))
	
import numpy as np
# Will timeout if feature map is computed
d = 100
k = monomial_kernel(d)
x = 0.1 * np.ones(100)
y = -0.02 * np.ones(100)
print(np.isclose(k(x, y), 5 / 6))