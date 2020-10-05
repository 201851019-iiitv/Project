##HW3
#P20: Page 169 Problem 20

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/lenovo/Desktop/HW3Solution/Module')

#change path accordingly .....................
from numpy import linspace, nan, sqrt, log
from newtonRaphson import *

# r = T1/T2
def f(r,gamma,eta): return ( -log(r) - (1. - r) ) / ( -log(r) + (1. - r)/(gamma - 1.) ) - eta
def df(r,gamma,eta):
    denom = log(r) - (1. - r)/(gamma - 1.)
    numer_1 = 1./r - 1
    numer_2 = ( log(r) + (1. - r) ) * ( 1./r + 1./(gamma - 1.) )
    return numer_1 / denom - numer_2 / denom**2

if __name__ == "__main__":

    eta = 0.3
    gamma = 5./3

    if True:
        xs = linspace( 0.01, 1, 100 )
        fs = [ f(_,gamma,eta) for _ in xs ]

        import pylab;
        pylab.plot( xs, fs );
        pylab.xlabel('x'); pylab.ylabel('f(x)');
        pylab.axhline(y=0,color='k')
        pylab.grid('on');
        pylab.show()

    r = newtonRaphson( lambda _: f(_,gamma,eta), lambda _: df(_,gamma,eta), 0.1, 0.3 )
    print ("T2/T1= ", 1./r)
