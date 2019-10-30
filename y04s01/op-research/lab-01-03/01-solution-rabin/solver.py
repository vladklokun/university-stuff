from scipy.optimize import linprog

# Objective function coefficients
c = [-1000, -800, -700]

# Upper bound ineqality constraints coefficients
A_ub = [
    [ 6,  7,  2],
    [ 5,  2,  8],
    [10,  8,  6],
]

# Upper bound inequality (less than) constraints vector
b_ub = [
    40,
    36,
    50
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
    bounds=[x1_bounds, x2_bounds, x3_bounds],
    method="simplex",
)

# Print the result
print(res)
