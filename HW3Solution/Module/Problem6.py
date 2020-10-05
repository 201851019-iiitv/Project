#!/usr/bin/env python
#
# Problem EPage 133
#
# PYTHONPATH=../../BookCode:$PYTHONPATH
#
from numpy import asarray, hstack
from polyFit import *

# Our data:
#
data = asarray( [ [ 1310, 10.2 ], [ 1810, 8.1 ], [ 1175, 11.9 ], [ 2360, 5.5 ], [ 1960, 6.8 ],
                  [ 2020, 6.8 ], [ 1755, 7.7 ], [ 1595, 8.9 ], [ 1470, 9.8 ], [ 1430, 10.2 ],
                  [ 1110, 13.2 ], [ 1785, 7.7 ] ] )
xData = data[:,0]
yData = data[:,1]

coeff = polyFit( xData, yData, 1 )
print ("coeff= ", coeff)
print ("std= ", stdDev(coeff,xData,yData))
