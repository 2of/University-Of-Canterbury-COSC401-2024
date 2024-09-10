from math import exp
import numpy as np





def softmax(z):
    out = [0]* len(z)
    denom = sum([exp(x) for x in z])
    for i,entry in enumerate(z): 
        out[i] = exp(entry) / denom
    return np.array(out)
    

import numpy
numpy.set_printoptions(precision=3, suppress=True)

z = numpy.array([1, -1])
print(softmax(z))



import numpy
numpy.set_printoptions(precision=3, suppress=True)

z = numpy.array([-1, -1, 2, -1])
print(softmax(z))

import numpy
numpy.set_printoptions(precision=3, suppress=True)

z = numpy.array([-1, -1, -1, -1])
print(softmax(z))