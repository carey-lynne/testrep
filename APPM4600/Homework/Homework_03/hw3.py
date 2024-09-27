import numpy as np
import matplotlib.pyplot as plt

def driver():

# *******************QUESTION 1(c)*************************
    u = lambda x: np.sin(x) - 2*x + 1
    a = 0
    b = np.pi/2
    tol = 1e-8
    
    [astar,ier,count] = bisection(u,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', u(astar))
    print(f"iterations used: {count}")
    print()

# *******************QUESTION 2(a)*************************
    f = lambda x: (x-5)**9
    a = 4.82
    b = 5.2
    tol = 1e-4

    [astar,ier,count] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))
    print(f"iterations used: {count}")
    print()

# *******************QUESTION 2(b)*************************
    g = lambda x: -1953125 + 3515625*x - 2812500*x**2 + 1312500*x**3 - 393750*x**4 + 78750*x**5 - 10500*x**6 + 900*x**7 - 45*x**8 + x**9

    [astar,ier,count] = bisection(g,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', g(astar))
    print(f"iterations used: {count}")
    print()
# *******************QUESTION 3(b)*************************
    v = lambda x: x**3 + x - 4
    a = 1
    b = 4
    tol = 1e-3

    [astar,ier,count] = bisection(v,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', v(astar))
    print(f"iterations used: {count}")   
    print("***************************************************")
# *******************QUESTION 5(a)*************************
    w = lambda x: x - 4*np.sin(2*x) - 3

    x_vals = np.linspace(-10,10,1000)
    y_vals = w(x_vals)

    plt.plot(x_vals, y_vals)
    plt.title('x - 4*np.sin(2*x) - 3')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.axhline(0, color = 'black', linewidth = 1)
    plt.axvline(0, color = 'black', linewidth = 1)
    plt.show()

# *****************************ROUTINES****************************************************

def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
    #   print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier, count]

driver()               

# *******************QUESTION 5(b)**************************  

def iteration(x):
    return -np.sin(2 * x) + (5 / 4) * x - 3 / 4

def fixedpt(f, x0, tol, Nmax):
    approximations = np.zeros((Nmax, 1))
    approximations[0] = x0
    count = 0
    while count < Nmax:
        count += 1
        x1 = f(x0)
        approximations[count] = x1

        if abs(x1 - x0) < tol:
            approximations = approximations[:count + 1]
            return approximations, count

        x0 = x1

    return approximations, Nmax

# ************************************************************
x0 = 5 
tol = 1e-10
Nmax = 200 

approximations, iterations = fixedpt(iteration, x0, tol, Nmax)

print(f"Root approximation after {iterations} iterations: {approximations[-1][0]}")
print()

# *****************************************************************
def compute_order(x, x_star):
    diff_1 = np.abs(x[1:, 0] - x_star)
    diff_2 = np.abs(x[:-1, 0] - x_star)
    fit = np.polyfit(np.log(diff_2), np.log(diff_1), 1)
    
    return fit

root_approx = approximations[-1][0]
compute_order(approximations, root_approx)