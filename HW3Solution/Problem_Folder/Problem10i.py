##HW3
#P18: Page 166 Problem 10

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/lenovo/Desktop/HW3Solution/Module')

#change path accordingly .....................
from numpy import sin, cos, linspace
from rootsearch import *
from brent import *
from ridder import *


def f(x): return x * sin(x) + 3 * cos(x) - x
def df(x): return sin(x) + x * cos(x) - 3 * sin(x) - 1

if __name__ == "__main__":
    if True:
        xs = linspace( -6, +6, 500 )
        fs = [ f(_) for _ in xs ]

        import pylab;
        pylab.plot( xs, fs );
        pylab.xlabel('x'); pylab.ylabel('f(x)');
        #pylab.hold('on')
        pylab.axhline(y=0,color='k')
        pylab.grid('on');
        pylab.show()

    a, b, dx = -6, 6, 0.01
    print ("The roots are: ")
    while True:
        x1, x2 = rootsearch( f, a, b, dx )
        if x1!=None:
            a = x2
            if not True:
                root = brent( f, x1, x2 )
            else:
                root = ridder( f, x1, x2 )
            if root != None : print (root)
        else:
            break
