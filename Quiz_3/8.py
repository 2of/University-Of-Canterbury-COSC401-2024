import math

def softmax(z):
    # Ensure z is a 2D array
    if len(z.shape) == 1:
        z = z.reshape(1, -1)
    
    exp_scores = numpy.exp(z - numpy.max(z, axis=1, keepdims=True))
    return exp_scores / numpy.sum(exp_scores, axis=1, keepdims=True)



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