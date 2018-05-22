import numpy as np
import theano
import theano_tutorial
import theano.tensor as T
from theano import function
from theano import pp


x = T.dscalar('x')
y = T.dscalar('y')

z = x + y

f = function([x, y], z)
print f(2, 3)

np.allclose(f(16.3, 12.1), 28.4)