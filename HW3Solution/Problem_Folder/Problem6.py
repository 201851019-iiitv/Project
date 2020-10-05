##HW3
#P15: Page 142 Problem 6

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/lenovo/Desktop/HW3Solution/Module')

from numpy import asarray, hstack
from polyFit import *


data = asarray( [ [ 1198, 11.90 ], [ 1715, 6.80 ], [ 2530,5.53 ], [ 2014,6.38 ], [ 2136, 5.53],
                  [ 1492, 8.50 ], [ 1652, 7.65 ], [ 1168, 13.60], [ 1492, 9.78 ], [ 1602,8.93 ],
                  [ 1192, 11.90 ], [2045,6.38 ] ] )
xData = data[:,0]
yData = data[:,1]

coeff = polyFit( xData, yData, 1 )
print ("coeff= ", coeff)
print ("std= ", stdDev(coeff,xData,yData))
