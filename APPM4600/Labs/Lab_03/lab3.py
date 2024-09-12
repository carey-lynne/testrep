import numpy as np

#                                           -- Bisection Method --
# This method approximates the roots of continuous functions by repeatedly halving the interval
# and choosing the subinterval where the sign changes.  This iteration continues until the 
# interval is sufficiently small and the midpoint can be taken as an approximation to the root
# 
#                           -- What is required for the bisection method to work? --
#   * the function must be continuous
#   * the initial interval f(a) and f(b) must have opposite signs
#   * a stopping criterion (max iterations) must be defined aka. the tolerance
#
#                                        -- Fixed Point Iteration --
# This method is used to solve equations of the form x = g(x) with the goal of finding a fixed point 
# of the function g(x) which is a point r such that r = g(r).  Fixed-point iteration is often applied 
# to solve nonlinear equations of form f(x) = 0 (for root finding) by reformulating through repeated 
# approximations.
# 

# Import bisection_example.py and run driver()
import bisection_example
bisection_example.driver()


#                                            -- EXERCISES --
# 1. f(x) = x**2*(x-1)
# a) (a,b) = (.5,2)
#               f(a) = f(.5) = -0.125
#               f(b) = f(2)  = 4
#  should be ok to use bisection method
# b) (a,b) = (-1,.5)
#               f(a) = f(-1) = -2
#               f(b) = f(.5) = -.125
#  bisection method shouldn't work because there's no change of sign
# c) (a,b) = (-1,2)
#               f(a) = f(-1) = -2
#               f(b) = f(2)  = 4
#  should be ok to use bisection method 
# It isn't possible for bisection method to find the root x=0. The root at x=0 doesn't change sign 
# in the interval about x=0, so the bisection method cant be applied.

print("-----------------------------------------")
from bisection_example import bisection # import bisection function from bisection_example.py 

def f(x):
    return x**2 * (x-1)

def run_bisection_1():
    intervals = [(.5,2), (-1,.5), (-1,2)]
    tol = 1e-7

    for a,b in intervals:
        print(f"Interval: ({a},{b})")  # interval being tested

        astar, ier = bisection(f,a,b,tol) # call bisection and find root appx
        if ier == 0:
            print(f"the approximate root is: {astar}") # print root
            print(f"f(astar) = {f(astar)}") # print function value at root
        else:
            print("Bisection method failed to find a root in interval ({a},{b})")
        
        print("ier =", ier) # note error message
        print()
run_bisection_1()

#
# 2. 
# a) f(x) = (x-1)(x-3)(x-5) in interval [a,b] = [.5,2]    
#    Yes, the behavior is as expected and the code is successful.  
#    The appx. root = 1.0000030517578122
# 
# b) f(x) = (x-3)(x-1)^2 in interval [a,b] = [0,2]
#    The behavior was as expected and the code was not successful
#    f(0) = -3
#    f(2) = -1
#    sign doesn't flip bisection method won't return a result
#     
# c) f(x) = sin(x) in interval [a,b] = ([0,.1], [.5,3/4*pi])
#    In the first interval the code successfully finds the root at its endpoint
#    x = a = 0 so the root is returned right away within the tolerance 1e-5.  But for the second interval
#    the sign doesn't flip thus the bisection method will not return a root.
# 

print("-----------------------------------------")
def f(x):
    return (x-1)*(x-3)*(x-5)

def run_bisection_2():
    interval = [(0,2.4)]
    tol = 1e-5

    for a,b in interval:
        print(f"Interval: ({a},{b})")

        astar, ier = bisection(f,a,b,tol) # call bisection and find root appx
        if ier == 0:
            print(f"the approximate root is: {astar}") # print root
            print(f"f(astar) = {f(astar)}") # print function value at root
        else:
            print("Bisection method failed to find a root in interval ({a},{b})")
        
        print("ier =", ier) # note error message
        print()
run_bisection_2()

def f(x):
    return (x-1)**2 *(x-3) 

def run_bisection_3():
    interval = [(0,2)]
    tol = 1e-5

    for a,b in interval:
        print(f"Interval: ({a},{b})")

        astar, ier = bisection(f,a,b,tol) # call bisection and find root appx
        if ier == 0:
            print(f"the approximate root is: {astar}") # print root
            print(f"f(astar) = {f(astar)}") # print function value at root
        else:
            print("Bisection method failed to find a root in interval ({a},{b})")
        
        print("ier =", ier) # note error message
        print()
run_bisection_3()

def f(x):
    return np.sin(x) 

def run_bisection_4():
    interval = [(0,.1),(.5,3*np.pi/4)]
    tol = 1e-5

    for a,b in interval:
        print(f"Interval: ({a},{b})")

        astar, ier = bisection(f,a,b,tol) # call bisection and find root appx
        if ier == 0:
            print(f"the approximate root is: {astar}") # print root
            print(f"f(astar) = {f(astar)}") # print function value at root
        else:
            print("Bisection method failed to find a root in interval ({a},{b})")
        
        print("ier =", ier) # note error message
        print()
run_bisection_4()

#
# 3.
#

print("-----------------------------------------")

from fixedpt_example import fixedpt

def f_a(x):
    return x * (1 + (7-x**5)/x**2)**3

def f_b(x):
    return x - (x**5 - 7)/x**2

def f_c(x):
    return x - (x**5 - 7)/(5*x**4)

def f_d(x):
    return x - (x**5 - 7)/12

x0 = 1
tol = 1e-10
Nmax = 100

fixed_point = 7**(1/5)

def run_fixedpt_routine():
    fixedpt_functions = [f_a,f_b,f_c,f_d]
    
    