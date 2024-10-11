import numpy as np

# (a) Iterate on this system numerically, using the iteration scheme
# | x_(n+1) | = | x_n | - | 1/6  1/18 || f(x_n, y_n) |,  n = 0,1,2,... 
# | y_(n+1) |   | y_n |   | 0    1/6  || g(x_n, y_n) |
# starting with x_0 = y_0 = 1 and check how well it converges
print("----------------------PART(a)---------------------------")
# non-linear set of equations 
f = lambda x,y: 3*x**2 - y**2
g = lambda x,y: 3*x*y**2 - x**3 - 1

#  x and y initials
x0 = 1
y0 = 1

# set max tolerance and max iterations
tol = 1e-5
nmax = 20

# iteration matrix
matrix = np.array([[1/6, 1/18],[0, 1/6]])

x_values = [x0]
y_values = [y0]
errors = []

for n in range(nmax):
    xn = x_values[-1]
    yn = y_values[-1]

    fn = f(xn, yn)
    gn = g(xn, yn)

    vector_new = np.dot(matrix, np.array([fn, gn]))
    xi = xn - vector_new[0]
    yi = yn - vector_new[1]

    x_values.append(xi), y_values.append(yi)

    print(f"iteration {n+1}: x_n = {xi}, y_n = {yi}")

    # check for convergence
    if abs(xi - xn) < tol and abs(yi - yn) < tol:
        print(f"converged after {n+1} iterations for tol = {tol}")
        break
    
    if n == nmax - 1:
        print("max iterations achieved NO CONVERGENCE")

# finding how it converges
    if n > 0: 
        error = np.sqrt((xi - x_values[-2])**2 + (yi - y_values[-2])**2)
        errors.append(error)

# convergence type through error ratios
if len(errors) > 1:
    linear_ratios = [errors[k] / errors[k-1] for k in range(1, len(errors))]
    quadratic_ratios = [errors[k] / errors[k-1]**2 for k in range(1, len(errors))]

    print("\nRatios for linear convergence (e_{n+1} / e_n):")
    print(linear_ratios)
    print("\nRatios for quadratic convergence (e_{n+1} / e_n^2):")
    print(quadratic_ratios) 
        
#  (b) Newtons method

print("----------------------PART(b)---------------------------")

dfdx = lambda x,y: 6*x
dfdy = lambda x,y: -2*y
dgdx = lambda x,y: 3*x*y**2 - 3*x**2 
dgdy = lambda x,y: 6*x*y

# note the tolerance and max iterations are defined above the rest is redefined
x0 = 1
y0 = 1

x_values = [x0]
y_values = [y0]
errors = []

for n in range(nmax):
    xn = x_values[-1]
    yn = y_values[-1]

    fn = f(xn, yn)
    gn = g(xn, yn)

    J = np.array([[dfdx(xn, yn), dfdy(xn, yn)],[dgdx(xn, yn), dgdy(xn,yn)]])
    F = np.array([fn,gn])

    delta = np.linalg.solve(J, F)

    xi = xn - delta[0]
    yi = yn - delta[1]
    x_values.append(xi)
    y_values.append(yi)
    
    error = np.sqrt((xi - xn)**2 + (yi - yn)**2)
    errors.append(error)

    print(f"Iteration {n+1}: x_n = {xi}, y_n = {yi}")

    if error < tol:
        print(f"Converged after {n+1} iterations with tol = {tol}")
        break

    if n == nmax - 1:
        print("Max iterations achieved: NO CONVERGENCE")

errors = [float(e) for e in errors]

# convergence type through error ratios
if len(errors) > 1:
    linear_ratios = [errors[k] / errors[k-1] for k in range(1, len(errors))]
    quadratic_ratios = [errors[k] / errors[k-1]**2 for k in range(1, len(errors))]

    print("\nRatios for linear convergence (e_{n+1} / e_n):")
    print(linear_ratios)
    print("\nRatios for quadratic convergence (e_{n+1} / e_n^2):")
    print(quadratic_ratios)

# 3) (c)

f = lambda x,y,z: x**2 + 4*y**2 + 4*z**2 - 16
f_x = lambda x,y,z: 2*x
f_y = lambda x,y,z: 8*y
f_z = lambda x,y,z: 8*z

x,y,z = 1,1,1

tol = 1e-10
nmax = 50
count = 0

for count in range(nmax):
    count+=1

    fx = f_x(x,y,z)
    fy = f_y(x,y,z)
    fz = f_z(x,y,z)
    f_val = f(x,y,z)

    d = f_val/(fx**2 + fy**2 + fz**2)

    x_new = x - d*fx
    y_new = y - d*fy
    z_new = z - d*fz

    epsilon = np.sqrt((x_new - x)**2 + (y_new - y)**2 + (z_new - z)**2)
    if epsilon < tol:
        print(f"converged in {count} iterations")
        break
    x,y,z = x_new, y_new, z_new

    print(f"(x,y,z) = {x}, {y}, {z}")
    print(f"f(x,y,z) = {f(x,y,z)}")