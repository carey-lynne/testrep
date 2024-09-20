import numpy as np
import numpy as np

# *********************************************************************************************************
# fixed-point iteration function
def fixedpt(f, x0, tol, Nmax):
    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    # vector for approximations
    approximations = np.zeros((Nmax, 1))
    approximations[0] = x0

    count = 0
    while count < Nmax:
        count += 1
        x1 = f(x0)
        approximations[count] = x1

        if abs(x1 - x0) < tol:
            approximations = approximations[:count + 1]  # remove unused entries
            return approximations, count 

        x0 = x1

    return approximations, Nmax 

# *********************************************************************************************************
# function to compute the order of convergence and constant without flatten
def compute_order(x, x_star):
    # p_{n+1}-p (from the second index to the end)
    diff_1 = np.abs(x[1:, 0] - x_star)  # Extract scalar using [n, 0] for 2D array
    # p_n-p (from the first to second-to-last index)
    diff_2 = np.abs(x[:-1, 0] - x_star)  # Extract scalar using [n, 0] for 2D array
    
    # linear fit to log of differences
    fit = np.polyfit(np.log(diff_2), np.log(diff_1), 1)
    
    print('The order equation is:')
    print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
    print('lambda = ' + str(np.exp(fit[1])))
    print('alpha = ' + str(fit[0]))
    
    return fit, diff_1, diff_2

# *********************************************************************************************************
# driver function
def driver():
    f1 = lambda x: np.sqrt(10 / (x + 4))
    x0 = 1.5
    Nmax = 100
    tol = 1e-10

    p = 1.3652300134140976

    # fixed-point iteration
    approximations, iterations = fixedpt(f1, x0, tol, Nmax)
    
    print(f"iterations converged in: {iterations}")
    print(f"final approximation: {approximations[-1][0]}") 

    # order of convergence and constant
    fit, diff_1, diff_2 = compute_order(approximations, p)

driver()

### EXERCISES ###
# 1)
# a) With the initial guess of p0 = 1.5, how many iterations does it take for the fixed point 
# iteration to converge with an absolute tolerance of 10−10?
# 
# with the initial guess of p0 = 1.5 it takes 12 iterations to converge with an absolute tolerance of 1e-10

# (b) Use the technique to developed in problem 1 to determine the order of convergence of
# the fixed point method. (You know this from class but it is good to practice numerically
# finding it.) Also determine the constant associated with this convergence rate.
# 
# the order of convergence is output as alpha = 0.9996909905165663  or appx 1 indicating fixed point converges linearly
# and and the error constant lambda = 0.1265274282031372
#
# 2)
#  