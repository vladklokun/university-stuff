"""
Variant 28

1 x_1 + 1 x_2 <= 15
2 x_1 + 5 x_2 <= 60
3 x_1 + 1 x_2 <= 30

x_1, x_2 >= 0

z = x_1^2 + x_2^2 - 18 x_1 - 20 x_2 → min.


# How to run
    ## Install the virtual environment and prerequisites
    ## You only need to do this ONCE
    python -m venv venv
    venv\Scripts\activate.bat
    pip install -r requirements.txt

    ## Run the script
    python qp-solver-var-26.py

# Expected output
    [[2. 0.]
     [0. 2.]] === P
    [[2. 0.]
     [0. 2.]] === P[2]
    [-18. -20.] === q
    [[ 1.  1.]
     [ 2.  5.]
     [ 3.  1.]
     [-1.  0.]
     [ 0. -1.]] === G
    [15. 60. 30.  0.  0.] === h

    The optimal value is: -173.00000000000003
    A solution x is: [7. 8.]
"""

import cvxpy as cp
import numpy as np

# Specify the problem coefficients
P = 2 * np.array([
    [1.0, 0.0],
    [0.0, 1.0],
])
q = np.array([-18.0, -20.0])
G = np.array([
    [ 1.0,  1.0],
    [ 2.0,  5.0],
    [ 3.0,  1.0],
    [-1.0,  0.0],
    [ 0.0, -1.0],
])
h = np.array([ 15.0, 60.0, 30.0, 0.0, 0.0])

print("{} === P".format(P))
print("{} === q".format(q))
print("{} === G".format(G))
print("{} === h".format(h))

# Define and solve the CVXPY problem.
# the decision variable has as many components as the dimension of coefficient
# matrix
x = cp.Variable(P.shape[0])
# Create the problem instance
prob = cp.Problem(
    cp.Minimize((1/2)*cp.quad_form(x, P) + q.T @ x),
    [
        G @ x <= h,
        # A @ x == b
    ]
)
prob.solve()

# Print result
print("\nThe optimal value is: {}".format(prob.value))
print("A solution x is: {}".format(x.value))

# Print dual solutions. Not required by the task.
"""
print(
    "A dual solution corresponding to the inequality constraints is: {}"
    .format(
        prob.constraints[0].dual_value
    )
)
"""
