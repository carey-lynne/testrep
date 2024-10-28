import numpy as np
import matplotlib.pyplot as plt

# 1.

def driver():
    f = lambda x: 1/(1 + x**2)
    fd = lambda x: -2*x/(1 + x**2)**2
    a = -5
    b = 5

    # number of nodes
    n = [5,10,15,20]
    
    # for subplotting on the same figure
    fig_a, axes_a = plt.subplots(2, 2, figsize=(12, 8))
    axes_a = axes_a.flatten()
    count = 0    

    # Lagrange Interpolation
    for i in n: 
        nodes = np.linspace(a,b, i+1) # define equispaced nodes
        y_values = np.array([f(x) for x in nodes]) # function values at nodes
        x_eval = np.linspace(a,b,1000) # x_eval points over interval [a,b]
        p_eval = np.array([lagrange_interpolant(x, nodes, y_values) for x in x_eval])

        axes_a[count].plot(x_eval, f(x_eval), label='f(x) = 1/(1 + x^2)', color='blue')
        axes_a[count].plot(x_eval, p_eval, label=f'Interpolant (n={i})', color='red', linestyle='--')
        axes_a[count].scatter(nodes, y_values, color='black', marker='o', label='Nodes')
        axes_a[count].set_title(f'Lagrange Interpolation (n={i})')
        axes_a[count].legend()
        axes_a[count].grid()
        count+=1

    plt.show()

    # Hermite Interpolation
    fig_b, axes_b = plt.subplots(2, 2, figsize=(12, 8))
    axes_b = axes_b.flatten()
    count = 0

    for i in n:
        nodes = np.linspace(a,b, i+1) # define equispaced nodes
        y_values = np.array([f(x) for x in nodes]) # function values at nodes
        z_values = np.array([fd(x) for x in nodes]) # derivitive values at nodes
        x_eval = np.linspace(a,b,1000) # x_eval points over interval [a,b]
        h_eval = np.array([hermite_interpolant(x, nodes, y_values, z_values) for x in x_eval])

        axes_b[count].plot(x_eval, f(x_eval), label='f(x) = 1/(1 + x^2)', color='blue')
        axes_b[count].plot(x_eval, h_eval, label=f'Interpolant (n={i})', color='red', linestyle='--')
        axes_b[count].scatter(nodes, y_values, color='black', marker='o', label='Nodes')
        axes_b[count].set_title(f'Hermite Interpolation (n={i})')
        axes_b[count].legend()
        axes_b[count].grid()
        count+=1

    plt.show()

    # Natural Cubic Spline
    fig_c, axes_c = plt.subplots(2, 2, figsize=(12, 8))
    axes_c = axes_c.flatten()
    count = 0

    for i in n:
        nodes = np.linspace(a,b, i+1) # define equispaced nodes
        y_values = np.array([f(x) for x in nodes]) # function values at nodes
        x_eval = np.linspace(a,b,1000) # x_eval points over interval [a,b]
        spline_eval = natural_cubic_spline(x_eval, nodes, y_values)

        axes_c[count].plot(x_eval, f(x_eval), label='f(x) = 1/(1 + x^2)', color='blue')
        axes_c[count].plot(x_eval, spline_eval, label=f'Interpolant (n={i})', color='red', linestyle='--')
        axes_c[count].scatter(nodes, y_values, color='black', marker='o', label='Nodes')
        axes_c[count].set_title(f'NCS (n={i})')
        axes_c[count].legend()
        axes_c[count].grid()
        count+=1

    plt.show()

    # Clamped Cubic Spline
    fig_d, axes_d = plt.subplots(2, 2, figsize=(12, 8))
    axes_d = axes_d.flatten()
    count = 0

    for i in n:
        nodes = np.linspace(a,b, i+1) # define equispaced nodes
        y_values = np.array([f(x) for x in nodes]) # function values at nodes
        x_eval = np.linspace(a,b,1000) # x_eval points over interval [a,b]
        spline_eval = clamped_cubic_spline(x_eval, nodes, y_values, fd)

        axes_d[count].plot(x_eval, f(x_eval), label='f(x) = 1/(1 + x^2)', color='blue')
        axes_d[count].plot(x_eval, spline_eval, label=f'Interpolant (n={i})', color='red', linestyle='--')
        axes_d[count].scatter(nodes, y_values, color='black', marker='o', label='Nodes')
        axes_d[count].set_title(f'CCS (n={i})')
        axes_d[count].legend()
        axes_d[count].grid()
        count+=1

    plt.show()


# Lagrange basis: L_j(x)
def lagrange_basis(x, nodes, j):
    numerator = 1
    denominator = 1

    for i in range(len(nodes)):
        if i!=j:
            numerator *= (x-nodes[i])
            denominator *= (nodes[j] - nodes[i])

    return numerator/denominator
    
# Lagrange interpolat: p_n(x) = sum L_j(x)f(x_j)
def lagrange_interpolant(x, nodes, y_values):
    p = 0

    for j in range(len(nodes)):
        L_jx = lagrange_basis(x, nodes, j)
        p += L_jx*y_values[j]

    return p

# Lagrange basis derivative at x_j: L_j'(x_j)
def lagrange_basis_derivative(nodes, j):
    sum = 0
    for i in range(len(nodes)):
        if i!= j:
            p = 1/(nodes[j]-nodes[i])
            sum += p
    return sum

# Hermite interpolant: z_values = f'(x_)
def hermite_interpolant(x, nodes, y_values, z_values):
    p = 0

    for j in range(len(nodes)):
        L_jx = lagrange_basis(x, nodes, j)
        dL_jx = lagrange_basis_derivative(nodes, j)
        H_j = L_jx**2 * (1 - 2*dL_jx*(x - nodes[j]))
        K_j = L_jx**2 * (x - nodes[j])
        p += H_j*y_values[j] + K_j*z_values[j]
    return p

# natural cubic spline
def natural_cubic_spline(x_eval, nodes, y_values):
    n = len(nodes)-1
    h = [nodes[i+1] - nodes[i] for i in range(n)]

    A = np.zeros((len(nodes), len(nodes)))
    b = np.zeros(len(nodes))

    # end conditions s_2"(x_0) = s_2"(x_m) = 0
    A[0,0] = 1
    A[n,n] = 1

    for i in range(1,n):
        A[i,i-1] = h[i-1]
        A[i,i] = 2*(h[i-1] + h[i])
        A[i,i+1] = h[i]

        b[i] = 6*((y_values[i+1] - y_values[i])/h[i] - (y_values[i] - y_values[i-1])/h[i-1])

    sigma = np.linalg.solve(A,b)

    spline_eval = np.zeros_like(x_eval)
    for i in range(n):
        mask = (x_eval >= nodes[i]) & (x_eval <= nodes[i + 1])
        xi = nodes[i]
        xi1 = nodes[i + 1]
        hi = h[i]

        # spline coefficients
        a = (sigma[i+1] - sigma[i]) / (6*hi)
        b = sigma[i]/2
        c = (y_values[i+1] - y_values[i])/hi - (2*hi*sigma[i] + hi*sigma[i+1])/6
        d = y_values[i]

        spline_eval[mask] = (a*(x_eval[mask] - xi)**3 + b*(x_eval[mask] - xi)**2 + c*(x_eval[mask] - xi) + d)

    return spline_eval

# clamped cubic spline
def clamped_cubic_spline(x_eval, nodes, y_values, fd):
    n = len(nodes)-1
    h = [nodes[i+1] - nodes[i] for i in range(n)]

    A = np.zeros((len(nodes), len(nodes)))
    b = np.zeros(len(nodes))

    # new end conditions
    A[0,0] = 2*h[0]
    A[0,1] = h[0]
    b[0] = 6*((y_values[1] - y_values[0])/h[0] - fd(nodes[0]))

    A[n,n] = 2*h[n-1]
    A[n,n-1] = h[n-1]
    b[n] = 6*(fd(nodes[n]) - (y_values[n] - y_values[n - 1])/h[n - 1])

    for i in range(1,n):
        A[i,i-1] = h[i-1]
        A[i,i] = 2*(h[i-1] + h[i])
        A[i,i+1] = h[i]

        b[i] = 6*((y_values[i+1] - y_values[i])/h[i] - (y_values[i] - y_values[i-1])/h[i-1])

    sigma = np.linalg.solve(A,b)

    spline_eval = np.zeros_like(x_eval)
    for i in range(n):
        mask = (x_eval >= nodes[i]) & (x_eval <= nodes[i+1])
        xi = nodes[i]
        xi1 = nodes[i+1]
        hi = h[i]

        # spline coefficients
        a = (sigma[i+1] - sigma[i])/(6*hi)
        b = sigma[i]/2
        c = (y_values[i+1] - y_values[i])/hi - (2*hi*sigma[i] + hi*sigma[i+1])/6
        d = y_values[i]

        spline_eval[mask] = (a*(x_eval[mask] - xi)**3 + b*(x_eval[mask] - xi)**2 + c*(x_eval[mask] - xi) + d)

    return spline_eval

# driver()




# 2.
# chebyshev nodes
def chebyshev_nodes(a, b, n):
    i = np.arange(n+1)
    x_cheb = np.cos((2*i + 1)*np.pi/(2*(n+1)))  # nodes in [-1, 1]
    return 0.5*(a+b) + 0.5*(b-a)*x_cheb  

def driver2():
    f = lambda x: 1/(1 + x**2)
    fd = lambda x: -2*x/(1 + x**2)**2
    a = -5
    b = 5

    # number of nodes
    n = [5,10,15,20]
    
    # for subplotting on the same figure
    fig_a, axes_a = plt.subplots(2, 2, figsize=(12, 8))
    axes_a = axes_a.flatten()
    count = 0    

    # Lagrange Interpolation
    for i in n: 
        nodes = chebyshev_nodes(a,b, i) # define chebyshev nodes
        y_values = np.array([f(x) for x in nodes]) # function values at nodes
        x_eval = np.linspace(a,b,1000) # x_eval points over interval [a,b]
        p_eval = np.array([lagrange_interpolant(x, nodes, y_values) for x in x_eval])

        axes_a[count].plot(x_eval, f(x_eval), label='f(x) = 1/(1 + x^2)', color='blue')
        axes_a[count].plot(x_eval, p_eval, label=f'Interpolant (n={i})', color='red', linestyle='--')
        axes_a[count].scatter(nodes, y_values, color='black', marker='o', label='Nodes')
        axes_a[count].set_title(f'Lagrange Interpolation (n={i})')
        axes_a[count].legend()
        axes_a[count].grid()
        count+=1

    plt.show()

    # Hermite Interpolation
    fig_b, axes_b = plt.subplots(2, 2, figsize=(12, 8))
    axes_b = axes_b.flatten()
    count = 0

    for i in n:
        nodes = chebyshev_nodes(a,b, i) # define chebyshev nodes
        y_values = np.array([f(x) for x in nodes]) # function values at nodes
        z_values = np.array([fd(x) for x in nodes]) # derivitive values at nodes
        x_eval = np.linspace(a,b,1000) # x_eval points over interval [a,b]
        h_eval = np.array([hermite_interpolant(x, nodes, y_values, z_values) for x in x_eval])

        axes_b[count].plot(x_eval, f(x_eval), label='f(x) = 1/(1 + x^2)', color='blue')
        axes_b[count].plot(x_eval, h_eval, label=f'Interpolant (n={i})', color='red', linestyle='--')
        axes_b[count].scatter(nodes, y_values, color='black', marker='o', label='Nodes')
        axes_b[count].set_title(f'Hermite Interpolation (n={i})')
        axes_b[count].legend()
        axes_b[count].grid()
        count+=1

    plt.show()

    # Natural Cubic Spline
    fig_c, axes_c = plt.subplots(2, 2, figsize=(12, 8))
    axes_c = axes_c.flatten()
    count = 0

    for i in n:
        nodes = chebyshev_nodes(a,b, i) # define chebyshev nodes
        y_values = np.array([f(x) for x in nodes]) # function values at nodes
        x_eval = np.linspace(a,b,1000) # x_eval points over interval [a,b]
        spline_eval = natural_cubic_spline(x_eval, nodes, y_values)

        axes_c[count].plot(x_eval, f(x_eval), label='f(x) = 1/(1 + x^2)', color='blue')
        axes_c[count].plot(x_eval, spline_eval, label=f'Interpolant (n={i})', color='red', linestyle='--')
        axes_c[count].scatter(nodes, y_values, color='black', marker='o', label='Nodes')
        axes_c[count].set_title(f'NCS (n={i})')
        axes_c[count].legend()
        axes_c[count].grid()
        count+=1

    plt.show()

    # Clamped Cubic Spline
    fig_d, axes_d = plt.subplots(2, 2, figsize=(12, 8))
    axes_d = axes_d.flatten()
    count = 0

    for i in n:
        nodes = chebyshev_nodes(a,b, i) # define chebyshev nodes
        y_values = np.array([f(x) for x in nodes]) # function values at nodes
        x_eval = np.linspace(a,b,1000) # x_eval points over interval [a,b]
        spline_eval = clamped_cubic_spline(x_eval, nodes, y_values, fd)

        axes_d[count].plot(x_eval, f(x_eval), label='f(x) = 1/(1 + x^2)', color='blue')
        axes_d[count].plot(x_eval, spline_eval, label=f'Interpolant (n={i})', color='red', linestyle='--')
        axes_d[count].scatter(nodes, y_values, color='black', marker='o', label='Nodes')
        axes_d[count].set_title(f'CCS (n={i})')
        axes_d[count].legend()
        axes_d[count].grid()
        count+=1

    plt.show()

driver2()

