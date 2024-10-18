import numpy as np
import numpy.linalg as solve

f = lambda x,y: x**2 +y**2 - 4
g = lambda x,y: np.exp(x) + y -1

def F(X):
    return np.array([f(X[0], X[1]), g(X[0], X[1])])

def jacobian(X):
    x, y = X
    return np.array([[2*x, 2*y],[np.exp(x), 1]])

def broyden(F, X0, tol = 1e-6, Nmax = 100):
    X = np.array(X0)
    B = jacobian(X)  

    for i in range(Nmax):
        F_values = F(X)
        if np.linalg.norm(F_values, ord=2) < tol:
            print(f"Broyden's converged: {i} iterations")
            return X
        
        delta_X = np.linalg.solve(B, -F_values)

        X_new = X + delta_X
        s = X_new - X
        y = F(X_new) - F_values

        B += np.outer((y-np.dot(B,s)),s)/ np.dot(s,s)
        
        X = X_new

    print("Broyden's didn't converge in max iterations")
    return X
# *************************************************************************
def newtons(F, X0, tol=1e-6, max_iter=100):
    X = np.array(X0, dtype=float)

    for i in range(max_iter):
        F_values = F(X)

        if np.linalg.norm(F_values, ord=2) < tol:
            print(f"Newton's converged: {i} iterations")
            return X

        J = jacobian(X)

        delta_X = np.linalg.solve(J, -F_values)

        X = X + delta_X

    print("Newton's did not converge in max iterations")
    return X

xy_initial = [(1,1), (1,-1), (0,0)]

# print("Broyden's:")
# for i in xy_initial:
#     r = broyden(F, i)
#     print(f"Initial guess {i}) => Solution: {r}\n")

# print("Newton's:")
# for i in xy_initial:
#     r = newtons(F, i)
#     print(f"Initial guess {i}) => Solution: {r}\n")

# *******************************************************************
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv, norm

def driver():
    Nmax = 100
    tol = 1e-6
    x0 = np.array([.5, .5, .5])

    x_newton, newton_its = newtons_method(x0, tol, Nmax)
    print(f"Newton: {newton_its} iterations, solution: {x_newton}")

    # Steepest Descent
    [x_steep, gval, ier, its_sd] = SteepestDescent(x0, tol, Nmax)
    print(f"steepest descent: {its_sd} iterations, solution: {x_steep}")

    # Steepest Descent then Newton's
    [x_steep_partial, gval, ier, its_sd_partial] = SteepestDescent(x0, 5e-2, Nmax)
    x_hybrid, newton_its_hybrid = newtons_method(x_steep_partial, tol, Nmax)
    print(f"Hybrid: {its_sd_partial} steepest descent iterations, {newton_its_hybrid} Newton iterations")
    print("Hybrid method solution: ", x_hybrid)


def evalF(x):
    F = np.zeros(3)
    F[0] = x[0] + math.cos(x[0]*x[1]*x[2]) - 1.
    F[1] = (1. - x[0])**(0.25) + x[1] + 0.05 * x[2]**2 - 0.15*x[2] - 1
    F[2] = -x[0]**2 - 0.1*x[1]**2 + 0.01*x[1] + x[2] - 1
    return F

def evalJ(x):
    J = np.array([[1-x[1]*x[2]*math.sin(x[0]*x[1]*x[2]), -x[0]*x[2]*math.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*math.sin(x[0]*x[1]*x[2])], [-1/(4*(1-x[0])**(3/4)), 1, 0.1 * x[2] - 0.15], [-2 * x[0], -0.2 * x[1] + 0.01, 1]])
    return J

def evalg(x):
    F = evalF(x)
    g = F[0]**2 + F[1]**2 + F[2]**2
    return g

def eval_gradg(x):
    F = evalF(x)
    J = evalJ(x)
    gradg = np.transpose(J).dot(F)
    return gradg

def SteepestDescent(x, tol, Nmax):
    for its in range(Nmax):
        g1 = evalg(x)
        z = eval_gradg(x)
        z0 = norm(z)

        if z0 == 0:
            print("zero gradient")
        z = z / z0
        alpha3 = 1
        dif_vec = x - alpha3 * z
        g3 = evalg(dif_vec)
        while g3 >= g1:
            alpha3 /= 2
            dif_vec = x - alpha3 * z
            g3 = evalg(dif_vec)
        if alpha3 < tol:
            print("no likely improvement")
            return [x, g1, 0]
        alpha2 = alpha3 / 2
        dif_vec = x - alpha2 * z
        g2 = evalg(dif_vec)

        h1 = (g2 - g1) / alpha2
        h2 = (g3 - g2) / (alpha3 - alpha2)
        h3 = (h2 - h1) / alpha3

        alpha0 = 0.5 * (alpha2 - h1 / h3)
        dif_vec = x - alpha0 * z
        g0 = evalg(dif_vec)

        if g0 <= g3:
            alpha = alpha0
            gval = g0
        else:
            alpha = alpha3
            gval = g3
        x = x - alpha * z
        if abs(gval - g1) < tol:
            return [x, gval, 0]
    return [x, g1, 1]

def newtons_method(x0, tol, Nmax):
    x = np.array(x0, dtype=float)
    for i in range(Nmax):
        F = evalF(x)
        if norm(F) < tol:
            print(f"Newton's converged: {i} iterations")
            return x, i  
        J = evalJ(x)
        delta_x = np.linalg.solve(J, -F)
        x = x + delta_x
    print("Newton's method did not converge within max iterations")
    return x, Nmax 

if __name__ == '__main__':

    .
    ``
    driver()

