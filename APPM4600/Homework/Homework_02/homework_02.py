import numpy as np
import matplotlib.pyplot as plt
import math


x = 9.999999995000000e-10
def f(x):
    y = math.exp(x)
    return (y-1)

print(f(x))

import numpy as np
import matplotlib.pyplot as plt
import random

# Part (a)
# Create vector t with entries starting at 0 incrementing by π/30 to π
t = np.arange(0, np.pi + np.pi/30, np.pi/30)
y = np.cos(t)

# Evaluate the sum S = sum(t(k) * y(k) for k in range N)
S = np.sum(t * y)

# Print the result
print(f"The sum is: {S}")

# Part (b) Wavy circles
R = 1.2
delta_r = 0.1
f = 15
p = 0

# Parametric plot for given values
theta = np.linspace(0, 2 * np.pi, 1000)
x = R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)
y = R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.title("Wavy Circle for R=1.2, δr=0.1, f=15, p=0")
plt.axis('equal')
plt.xlabel('x(θ)')
plt.ylabel('y(θ)')
plt.grid(True)
plt.show()

# Multiple wavy circles with varying parameters
plt.figure(figsize=(6, 6))
for i in range(1, 11):
    R = i
    delta_r = 0.05
    f = 2 + i
    p = random.uniform(0, 2)  # Random p between 0 and 2
    x = R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)
    y = R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)
    plt.plot(x, y, label=f'R={R}, f={f}, p={p:.2f}')

plt.title("Multiple Wavy Circles")
plt.axis('equal')
plt.xlabel('x(θ)')
plt.ylabel('y(θ)')
plt.legend(loc='upper right', fontsize='small')
plt.grid(True)
plt.show()