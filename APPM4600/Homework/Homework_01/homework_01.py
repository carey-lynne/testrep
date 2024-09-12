import numpy as np
import matplotlib.pyplot as plt

# Question 1

# (i) p(x) = (x−2)**9 = x**9 −18x**8 +144x**7 −672x**6 +2016x**5 −4032x**4 +5376x**3 −4608x**2 +2304x−512
# Plot p(x) for x = 1.920, 1.921, 1.922, . . . , 2.080 (i.e. x = [1.920 : 0.001 : 2.080];)
# evaluating p via its coefficients

def p_coeff(x):
    return x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512

x = np.arange(1.920, 2.081, 0.001)

y = p_coeff(x)

plt.plot(x, y, label = "(evaluation of p via coefficients)")
plt.title("Evaluation of p via Coefficients")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.grid(True)
plt.show()

# (ii) roduce the same plot again, now evaluating p via the expression (x − 2)**9
def p_expression(x):
    return (x-2)**9

z = p_expression(x)

plt.plot(x, z, label = "(evaluation of p via expression)")
plt.title("Evaluation of p via Expression")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.grid(True)
plt.show()
