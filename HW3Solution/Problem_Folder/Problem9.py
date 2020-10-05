##HW3
#P16: Page 143 Problem 9

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/lenovo/Desktop/HW3Solution/Module')

from numpy import asarray, hstack
from polyFit import *
from evalPoly import evalPoly

# Our data:
#
xData = asarray( [ 1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7 ] )
yData = asarray( [ 6.008, 15.722, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828 ] )

for degree in [ 1, 2 ] :
    coeff = polyFit( xData, yData, degree )
    s = stdDev(coeff,xData,yData)
    print ("degree= %5d; sigma= %10.6f with coeff= %s" % (degree,s,coeff))
