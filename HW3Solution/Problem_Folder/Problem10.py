##HW3
#P17: Page 143 Problem 10

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/lenovo/Desktop/HW3Solution/Module')

#change path accordingly .....................

from numpy import asarray, hstack
from polyFit import *
from evalPoly import evalPoly

# Our data:
#
data = asarray( [ [ 1718, 0.5 ], [ 1767, 0.8 ], [ 1774, 1.4 ], [ 1775, 2.7 ],
                  [ 1792, 4.5 ], [ 1816, 7.5 ], [ 1828, 12.0 ], [ 1834, 17.0 ],
                  [ 1878, 17.2 ], [ 1906, 23.0 ] ] )
xData = data[:,0]
yData = data[:,1]

for degree in [ 1, 2, 3, 4, 5, 6, 7 ] :
    coeff = polyFit( xData, yData, degree )
    s = stdDev(coeff,xData,yData)
    print ("degree= %5d; sigma= %10.6f" % (degree,s))
