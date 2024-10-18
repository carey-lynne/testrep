import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv



### PRE-LAB ###
#  Write a subroutine that constructs and evaluates a line that goes through the points (x0, f (x0)) and (x1, f (x1)) at a point α
def eval_line(x0, y0, x1, y1, alpha):
    m = (y1 -y0)/(x1 - x0)
    b = y0 - m*x0
    return m*alpha + b

### LAB ###
def eval_lin_spline(xeval, Neval, a, b, f, Nint):
    # create intervals for piecewise approximations
    xint = np.linspace(a,b,Nint+1)

    # create vector to store the evaluation of linear splines
    yeval = np.zeros(Neval)

    for jint in range(Nint):
        # find indices of xeval in interval (xint(jint),xint(jint+1))
        # let ind denote the indices in the intervals        
        atmp = xint[jint]
        btmp = xint[jint+1]

        # find indices of values of xeval in the interval
        ind = np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]
        n = len(xloc)

        # # debug statement  NOTE TO SELF FIGURED OUT I ACCIDENTILY PUT MY RETURN STATEMENT IN MY FIRST FOR LOOP
        # print(f"Interval {jint}: [{atmp}, {btmp}]")
        # print(f"xloc = {xloc}")


        # temp store your info for creating a line in the interval of interest
        fa = f(atmp)
        fb = f(btmp)

        yloc = np.zeros(len(xloc))
        for kk in range(n):
            # use line evaluator to evaluate the spline at each location
            yloc[kk] = eval_line(atmp, fa, btmp, fb, xloc[kk])

        # copy yloc into the final vector
        yeval[ind] = yloc
    return yeval
        
def driver():
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1

    # '''create points you want to evaluate at'''
    Neval = 100
    xeval = np.linspace(a,b,Neval)

    # '''number of intervals'''
    Nint = 20

    # '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval, Neval, a, b, f, Nint)

    # "evaluate f at the evaluation points"
    fex = f(xeval)

    plt.figure()
    plt.plot(xeval, fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    plt.legend(loc='best')
    plt.show()

    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show()

driver()
        
### EXERCISE ###
# 3.2) Consider the function f(x) = 1/(1+(10x)**2) on interval [-1,1].  
#      Preform the same experiments in Lab 7 but with the linear spline evaluator:
# 
#   the linear spline performs well and as it should, it preforms better than global interpolation with uniform nodes
    