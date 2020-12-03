import numpy as np


def output(array, t, filename = "9"):
    array = np.insert(array, 0, t)
    with open(filename, "a") as g:
        np.savetxt(g, [array], fmt="%.4f")


# Problem 3: Finite differences
# Implicit Solution

# solve case 1 of the smith paper
# compare results at x = 0.3, t = 0.01, 0.02, 0.10

# -------------------------------------------------

# initialize a matrix for case 1:
A = np.array([[0],
             [0.2],
             [0.4],
             [0.6],
             [0.8],
             [1],
             [0.8]])  # stop here because it is symmetrical

dx = 0.1
alpha = 1
dt = 0.001
a = dx**2 / alpha / dt

# ---------------------------------------------

# Explicit Solution:
A0 = np.copy(A)
A1 = np.copy(A)
t = 0
while round(t, 3) <= 0.100:
    # save the profile at each t
    global Explicit_At000, Explicit_At001, Explicit_At002, Explicit_At010
    if round(t, 3) == 0:
        Explicit_At000 = np.copy(A1)
    elif round(t, 3) == 0.010:
        Explicit_At001 = np.copy(A1)
    elif round(t, 3) == 0.020:
        Explicit_At002 = np.copy(A1)
    elif round(t, 3) == 0.100:
        Explicit_At010 = np.copy(A1)

    for i in range(1,6):
        A1[i] = A0[i] + (1 / a) * (A0[i-1] - 2 * A0[i] + A0[i+1])

    A1[6] = A1[4]
    A0 = np.copy(A1)
    t += dt

print('Explicit Solution')
print('t=0.00, x=0.3', Explicit_At000[3][0])
print('t=0.01, x=0.3', Explicit_At001[3][0])
print('t=0.02, x=0.3', Explicit_At002[3][0])
print('t=0.10, x=0.3', Explicit_At010[3][0])
print()

# --------------------------------------------

# Implicit Solution:
'''
Approach:
A1[i] = A0[i] + (dt * alpha / (dx**2)) * (A1[i-1] - 2 * A1[i] + A1[i+1])
A1[i] - (dt * alpha / (dx**2)) * (A1[i-1] - 2 * A1[i] + A1[i+1]) = A0[i]
A1[i] * ((dx**2) / (dt * alpha) + 2) - (A1[i-1]  - A1[i+1]) = (dx**2) / (dt * alpha) * A0[i]
implement equation above: a = 
x position: [0      0.1     0.2     0.3     0.4     0.5     0.6]   [x] = [A0]
            [-1     a+2       -1      0       0       0       0]   [x] = a * A0[1]
            [0      -1      a+2      -1       0       0       0]   [x] = a * A0[2]
            etc.
'''
AI = np.copy(A[1:6])
t = 0
Form = np.array([[a+2, -1, 0, 0, 0],
                 [-1, a+2, -1, 0, 0],
                 [0, -1, a+2, -1, 0],
                 [0, 0, -1, a+2, -1],
                 [0, 0, 0, -2, a+2]])

while round(t, 3) <= 0.100:
    # save the profile at each t
    global Implicit_At000, Implicit_At001, Implicit_At002, Implicit_At010
    if round(t, 3) == 0.00:
        Implicit_At000 = np.copy(AI)
        output(AI, t)
    elif round(t, 3) == 0.010:
        Implicit_At001 = np.copy(AI)
        output(AI, t)
    elif round(t, 3) == 0.020:
        Implicit_At002 = np.copy(AI)
        output(AI, t)
    elif round(t, 3) == 0.100:
        Implicit_At010 = np.copy(AI)
        output(AI, t)

    AI = np.copy(np.linalg.solve(Form, a*AI))
    t += dt

# todo: implicit values look a little high
print('Implicit Solution')
print('t=0.00, x=0.3', Implicit_At000[2][0])
print('t=0.01, x=0.3', Implicit_At001[2][0])
print('t=0.02, x=0.3', Implicit_At002[2][0])
print('t=0.10, x=0.3', Implicit_At010[2][0])
print()

# --------------------------------------------

# Analytical Solution:
def analytical_heat_eq(x, t, steps=500):
    # calculate a value from the equation on page 15
    pi = np.pi
    nsum = 0
    for n in range(1, steps):  # recommended n value on homework description
        nsum += 1/n**2 * np.sin(0.5 * n * pi) * np.sin(n * pi * x) * np.exp(-1*n**2 * pi**2 * t)
    U = 8 / pi**2 * nsum
    U = round(U, 4)  # output is more readable
    return U


print('Analytical Solution')
print('t=0.00, x=0.3', analytical_heat_eq(0.3, 0.00))
print('t=0.01, x=0.3', analytical_heat_eq(0.3, 0.01))
print('t=0.02, x=0.3', analytical_heat_eq(0.3, 0.02))
print('t=0.10, x=0.3', analytical_heat_eq(0.3, 0.10))

