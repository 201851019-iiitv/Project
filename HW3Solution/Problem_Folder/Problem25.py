##HW3
#P21: Page 170 Problem 25

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/lenovo/Desktop/HW3Solution/Module')

#change path accordingly .....................
from numpy import linspace, asarray, nan, sqrt, cos, sin, tan, arcsin, pi
from newtonRaphson2 import *
import numpy as np

def f(x) :
    f = np.zeros( (len(x)) )
    f[0] = tan(x[0]) - x[1]
    f[1] = cos(x[0]) - 3 * sin(x[1])
    return f


if __name__ == "__main__":

    if False:
        import pylab;
        pylab.hold('on')
        pylab.grid('on')

        xs = linspace( 0.01, 1.5-0.01, 200 )

        y1s = [ tan(_) for _ in xs ]
        pylab.plot( xs, y1s, color='b', label='tan' )

        max_y1 = max(y1s)

        y2s = asarray( [ arcsin(cos(_)/3.) for _ in xs ] )
        min_y2 = min(y2s)
        k = 0
        while (min_y2 + 2 * pi * k) < max_y1 :
            pylab.plot( xs, y2s + 2*pi*k, color='g', label='arcsin(k=%d)' % k )
            k += 1

        pylab.xlabel('x');
        pylab.axhline(y=0,color='k')
        pylab.axvline(x=0,color='k')
        pylab.legend(loc=0)
        pylab.show()

    print ("intersection 1= " )
    print (newtonRaphson2( f, [0.3,0.25] ))

    print ("intersection 2= ")
    print (newtonRaphson2( f, [1.4,6.3] ))
