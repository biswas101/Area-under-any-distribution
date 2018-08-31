# this script will integrate the area of any Distribution (Not necessarily a Gaussian Dist.)
# If there is positive or negative vallay, it will make vector sum and show net result
# This will do the integartion manually, ie. making slice and adding
# In this script we consider scatter type distribution, ie. its not continues
# Author:  Jyoti Biswas

from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
from numpy import genfromtxt
from traitlets.traitlets import add_article


fig = plt.figure()
ax1 = fig.add_subplot(111)

#D_mag= genfromtxt('bfield.txt',delimiter='',dtype=None, names=True)#
D_mag= genfromtxt('1st_Xtrim_3mm.txt',delimiter='',dtype=None, names=True)

X=np.array(D_mag['Z'])
Y=np.array(D_mag['B'])


# our distribution is inverted, hence we use .min
Yo_neg=Y.min()
Yo_pos=Y.max()
Ycut_neg= abs(Yo_neg/1000)     # Value lower that Cut off, is not considered in calculation


print("number of points:",len(X))
print("Min B field, Bo: ", Yo_neg)
print("Max B field, Bo: ", Yo_pos)

print("Cut off B field(abs.):", Ycut_neg)

val_neg = 0.0

for i in range(len(X)-1):
    if abs(Y[i] - X[i])>Ycut_neg:
        val_neg = val_neg + (X[i+1]-X[i])*Y[i] + 0.5*(X[i+1]-X[i])*(Y[i+1] - Y[i])


print("Area (vector sum):", val_neg)

ax1.scatter(X,Y, s=10, c='b', marker="o", label='B-field')
plt.legend(loc='upper right');

plt.grid()
plt.show()


