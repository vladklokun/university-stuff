from scipy.optimize import linprog

# Objective function coefficients
c = [-4, -3, 2]

# Ineqality contraints coefficients
A_ub = [
    [-1, -1, 0],
    [0, 0, 1],
]

# Inequality (less than) constraints vector
b_ub = [
    2,
    -5
]

# Equality constraints coefficients
A_eq = [
    [-2, -2, 1],
]
# Equality constraints vector
b_eq = [
    4,
]

# Variable bounds (x_{1, 2, 3} \geqslant 0)
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)

# Solve the problem
res = linprog(
    c=c,
    A_ub=A_ub,
    b_ub=b_ub,
    A_eq=A_eq,
    b_eq=b_eq,
    bounds=[x1_bounds, x2_bounds, x3_bounds],
    method="revised-simplex",
)

# Print the result
print(res)
