import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.linalg import inv
from numpy.linalg import solve


# function to interpolate 
f = lambda x: 1/ 1+(10*x**2)
a = -1
b = 1

# create eval points (1000 in [a,b])
Neval = 1000
xeval =  np.linspace(a,b,Neval)

# create interpolation nodes for n nodes

def create_nodes(N):   
    h = 2/(N-1) # step size per lab instructions
    x_nodes = [] 

    for j in range(N + 1):
        x_nodes.append(-1 + (j-1)*h)
    
    return np.array(x_nodes)


N = 10
x_nodes = create_nodes(N+1)
y_nodes = f(x_nodes)

# for i in range(N+1):
#     print(f"xnode = {x_nodes[i+1]}, ynode = {y_nodes[i+1]}")


# define and return vandermonde matrix for nodes
def vandermonde(x_nodes):
    N = len(x_nodes)
    V = np.vander(x_nodes, N, increasing=True)

    return V

# solve for monomial expansion coefficients
def monomial_exp(x_nodes, y_nodes):
    V = vandermonde(x_nodes)
    a = solve(V, y_nodes)

    return a

# evaluate monomial expansion at xeval
def evaluate_monomial_exp(a, xeval):
    yeval = np.zeros(len(xeval))
    N = len(a)

    for i in range(N):
        yeval += a[i]*(xeval**i)
    return yeval

#  get coeff and evaluate
a_monomial = monomial_exp(x_nodes, y_nodes)
yeval_monomial = evaluate_monomial_exp(a_monomial, xeval)

f_exact = f(xeval)

# plot
plt.figure(figsize=(10, 6))
plt.plot(xeval, f_exact, 'k-', label='Exact f(x)', linewidth=2)
plt.plot(xeval, yeval_monomial, 'r--', label='Monomial Expansion')
plt.legend()
plt.title('Interpolation Approximations')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# Plot the absolute error
plt.figure(figsize=(10, 6))
plt.semilogy(xeval, np.abs(f_exact - yeval_monomial), 'r--', label='Monomial Error')
plt.legend()
plt.title('Interpolation Errors')
plt.xlabel('x')
plt.ylabel('Absolute Error')
plt.grid(True)
plt.show()
