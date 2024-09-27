# PRE-LAB EXERCISE
# --- Method ---        --- Input ---                --- Iteration ---          --- Idea Behind Method ---        |      --- Required For Convergence --- |     --- Pros ---                | --- Cons ---
#               |   function to bisect = f  | midpoint = (b-a)/2         | if a root exists in the specified      | in order for convergence we must      |- will always find a root if it exists in the| - slow       
#               |   starting endpoint = a   | if the sign of midpoint    | interval the the sign of the evaluated | have opposing signs at f(a) and f(b)  |  interval with evaluated sign change        | - must be able to find an interval
#  Bisection    |   ending endpoint = b     | is the same as the sign of | function changes and we know a root    | ie. f(a)*f(b) < 0                     |- simple algorithm                           | - cant find a root without a sign change (think parabolic function with root of 0 at min)
#               |   tolerance = tol         | f(a), the root lies in     | exists in that interval if we halve the| This indicates a root by IVT          |- at every iteration the max err is halved   | - maybe if the interval gets very very small then subtraction by nearly equal numbers
#               |                           |[midpoint, b] else          | interval enough times we find a        |                                       |  giving a clear err estimate and rate of    |
#               |                           |[a, midpoint] repeat with   | midpoint within a specified tolerance  |                                       |  conversion                                 |
#               |                           |interval until tol is met   | which approximates the root            |                                       |- converges at linear rate                   |
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#               | function used in fp = f   | x_{n+1} = g(x_n)           | iteratively apply a function g(x)
#               | initial guess = x0        |                            | such that 
#  Fixed Point  | max # of iterations = Nmax|                            |
#               | tolerance = tol           |                            |
#               |                           |                            |
#               |                           |                            |
#               |                           |                            | 
# 
# 
# 










# EXERCISES
# 1) Viewing Newton's method as a fixed point method, derive a condition which guarentees that Newton's method 
#  will converge to a unique root for all initial guesses in a neighborhood of the root 
#  
# the iteration of Newton's method is given by, x_n+1 = x_n - f(x_n)/f'(x_n) then one can rewrite the iteration in a fixed point form so
# g(x) = x - f(x)/f'(x), then if we take the derivative of g(x) we end up with f(x)f"(x)/(f'(x))**2. For Newton's to 
# converge f(x)f"(x)/(f'(x))**2 < 1 thus this is the condition for the basin of convergence 
# 
# 
# 2) Bisection code which terminates when midpoint lies in basin of convergence for Newton's method
import numpy as np
def bisection_newton_convergence(f, df, ddf, a, b, tol):
    # Inputs:
    #  f, df, ddf - function f, f', f"
    #  a, b       - endpoints of initial interval
    #  tol        - bisection stops when interval length < tol

    # Returns:
    #  astar - approximation of root
    #  ier   - error message
    #        - ier = 1 => Failed
    #        - ier = 0 => Success
    
    # first verify there is a root we can find in the interval
    fa = f(a)
    fb = f(b)
    if (fa * fb > 0):
        ier = 1
        astar = a
        return [astar, ier]

    # verify endpoints are not a root 
    if (fa == 0):
        astar = a
        ier = 0
        return [astar, ier]

    if (fb == 0):
        astar = b
        ier = 0
        return [astar, ier]

    count = 0
    d = 0.5 * (a + b)
    
    # continue until the interval is small or midpoint is in basin of convergence
    while (abs(d - a) > tol):
        fd = f(d)
        if (fd == 0):
            astar = d
            ier = 0
            return [astar, ier]

        # if the midpoint lies in the basin of convergence for Newton's method return 
        if abs(f(d) * ddf(d) / (df(d)**2)) < 1:
            astar = d
            ier = 0
            return [astar, ier]

        # standard bisection
        if (fa * fd < 0):
            b = d
        else:
            a = d
            fa = fd

        d = 0.5 * (a + b)
        count = count + 1

    astar = d
    ier = 0
    return [astar, ier]

# 3) Do you need to change the input of the original bisection method? If so how did it change?
#  
# Yes I needed to change the input of the original bisection method.
# it changed only by having to add the first and second derivatives of the function f
# 
# 
# 4) Appending to your modified bisection code put Newton's method code but set it up so that it takes 
# the midpoint found by the bisection code method as input.



