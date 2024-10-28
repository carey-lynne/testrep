import numpy as np
import matplotlib.pyplot as plt

# #  define Vandermonde matrix V
# def vandermonde(x):
#     n = len(x)
#     V = np.zeros((n,n))
#     for i in range(n):
#         for j in range(n):
#             V[i,j] = x[i]**j  # [(x_i)**0, (x_i)**1,...,(x_i)**n]

#     return V

# # solve for coefficients: c = [c_1,...,c_n]^T
# def coefficients(x,y):
#     V = vandermonde(x)
#     V_inv = np.linalg.inv(V)
#     c = np.dot(V_inv,y)
#     return c

    
# # construct polynomial: p(x) = c_n + (c_n-1)x + ... + (c_1)x**(n-1)
# def construct_polynomial(c, x):
#     return np.polyval(c[::-1], x) 


# def driver():
#     f = lambda x: 1/(1+(10*x)**2)
#     a = -1
#     b = 1
#     N = 2

#     while True:
#         print(f"N = {N}")

#         # N uniformly spaced nodes in [a, b]
#         x_nodes = np.linspace(a,b,N)
#         y_nodes = f(x_nodes)

#         c = coefficients(x_nodes, y_nodes)

#         # finer grid
#         x_grid = np.linspace(a,b,1001)
#         y_grid = f(x_grid)
#         polynomial = construct_polynomial(c, x_grid)

#         # max value of the polynomial to see when it exceeds 100
#         max_val = np.max(np.abs(polynomial))

#         plt.plot(x_grid, y_grid, label="Function f(x)")
#         plt.plot(x_grid, polynomial, label=f"Polynomial N={N}", linestyle='--')
#         plt.plot(x_nodes, y_nodes, 'o', label="Interpolation nodes")
#         plt.legend()
#         plt.show()

#         if max_val > 100:
#             print(f"exceeded 100 for N = {N}")
#             break

#         N += 1

# driver()


# *****************************************************************************************
# 2) and 3)
# CHebyshev nodes
def chebyshev_nodes(a, b, N):
    j = np.arange(1, N+1)
    x = np.cos((2*j - 1)/(2*N) * np.pi)
    return ((b - a)*x)/2 + (b+a)/2

# define weights  
def barycentric_weights(x_nodes):
    n = len(x_nodes)
    w = np.ones(n)
    # loop to calc weights for all i != j
    for j in range(n):
        for i in range(n):
            if i!=j:
                w[j] = w[j]/(x_nodes[j]-x_nodes[i])

    return w

# barycentric Lagrange interpolation
def barycentric_lagrange(x_nodes, y_nodes, x_grid, w):
    p_num = np.zeros_like(x_grid)
    p_denom = np.zeros_like(x_grid)
    n = len(x_nodes)
    m = len(x_grid)

    # loop through and calc the sums for the numerator and denom of p(x)
    for j in range(n):
        for i in range(m):
            if abs(x_grid[i] - x_nodes[j]) < 1e-10: # nearly equal numbers and 0
                p_num[i] = y_nodes[j]               # set the numerator = f(x_j)
                p_denom[i] = 1                      # let denominator = 1
            else:
                # use barycentric formula
                weight_term = w[j] / (x_grid[i] - x_nodes[j])
                p_num[i] += weight_term * y_nodes[j]
                p_denom[i] += weight_term

    # polynomial values 
    p = np.zeros_like(x_grid)
    for i in range(len(x_grid)):
        if p_denom[i] != 0:
            p[i] = p_num[i] / p_denom[i]
        else:
            p[i] = 0

    return p     
    

def driver2():
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
    N = 2

    while True:
        print(f"N = {N}")

        # N uniformly spaced nodes in [a, b]
        x_nodes = np.linspace(a, b, N)
        y_nodes = f(x_nodes) 
        weights = barycentric_weights(x_nodes)

        # finer grid
        x_grid = np.linspace(a, b, 1001)
        y_grid = f(x_grid)
        polynomial = barycentric_lagrange(x_nodes, y_nodes, x_grid, weights)

        plt.plot(x_grid, y_grid, label="Function f(x)")
        plt.plot(x_grid, polynomial, label=f"Polynomial N={N}", linestyle='--')
        plt.plot(x_nodes, y_nodes, 'o', label="Interpolation nodes")
        plt.legend()
        plt.show()

        # max value of the polynomial to see when it exceeds 100
        max_val = np.max(np.abs(polynomial))

        if max_val > 100:
            print(f"exceeded 100 for N = {N}")
            break

        N += 1  # Increase N for the next iteration

# driver2()

# *********************************************************
def chebyshev_nodes(a, b, N):
    j = np.arange(1, N+1)
    x = np.cos((2*j - 1)/(2*N) * np.pi)
    return ((b - a)*x)/2 + (b+a)/2

# define weights  
def barycentric_weights(x_nodes):
    n = len(x_nodes)
    w = np.ones(n)
    # loop to calc weights for all i != j
    for j in range(n):
        for i in range(n):
            if i!=j:
                w[j] = w[j]/(x_nodes[j]-x_nodes[i])

    return w

# barycentric Lagrange interpolation
def barycentric_lagrange(x_nodes, y_nodes, x_grid, w):
    p_num = np.zeros_like(x_grid)
    p_denom = np.zeros_like(x_grid)
    n = len(x_nodes)
    m = len(x_grid)

    # loop through and calc the sums for the numerator and denom of p(x)
    for j in range(n):
        for i in range(m):
            if abs(x_grid[i] - x_nodes[j]) < 1e-10 & i != j: # nearly equal numbers and 0
                p_num[i] = y_nodes[j]               # set the numerator = f(x_j)
                p_denom[i] = 1                      # let denominator = 1
            else:
                # use barycentric formula
                weight_term = w[j] / (x_grid[i] - x_nodes[j])
                p_num[i] += weight_term * y_nodes[j]
                p_denom[i] += weight_term

    # polynomial values 
    p = np.zeros_like(x_grid)
    for i in range(len(x_grid)):
        if p_denom[i] != 0:
            p[i] = p_num[i] / p_denom[i]
        else:
            p[i] = 0

    return p     
    

def driver3():
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
    N = 2

    while True:
        print(f"N = {N}")

        # N uniformly spaced nodes in [a, b]
        x_nodes = chebyshev_nodes(a,b,N)
        y_nodes = f(x_nodes) 
        weights = barycentric_weights(x_nodes)

        # finer grid
        x_grid = np.linspace(a, b, 1001)
        y_grid = f(x_grid)
        polynomial = barycentric_lagrange(x_nodes, y_nodes, x_grid, weights)

        plt.plot(x_grid, y_grid, label="Function f(x)")
        plt.plot(x_grid, polynomial, label=f"Polynomial N={N}", linestyle='--')
        plt.plot(x_nodes, y_nodes, 'o', label="Interpolation nodes")
        plt.legend()
        plt.show()

        # max value of the polynomial to see when it exceeds 100
        max_val = np.max(np.abs(polynomial))

        if max_val > 100:
            print(f"exceeded 100 for N = {N}")
            break

        N += 1  # Increase N for the next iteration

driver3()

