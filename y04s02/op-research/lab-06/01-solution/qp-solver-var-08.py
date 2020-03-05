# Import packages.
import cvxpy as cp
import numpy as np

P = 2 * np.array([
    [4.0, 0.0],
    [0.0, 4.0],
])
q = np.array([8.0, -2.0])
G = np.array([
    [-1.0, -1.0],
    [ 2.0,  1.0],
    [ 1.0,  2.0],
    [-1.0,  0.0],
    [ 0.0, -1.0],
])
h = np.array([-1.0, 4.0, 6.0, 0.0, 0.0])
A = np.array([
    [-1.0, -1.0],
    [ 2.0,  1.0],
    [ 1.0,  2.0],
])
b = np.array([1.0, 4.0, 6.0])

print("P = {}".format(P))
print("P[2] = {}".format(P))
print("q = {}".format(q))
print("G = {}".format(G))
print("h = {}".format(h))
print("A = {}".format(A))
print("b = {}".format(b))

# Define and solve the CVXPY problem.
x = cp.Variable(P.shape[0])
prob = cp.Problem(
    cp.Minimize((1/2)*cp.quad_form(x, P) + q.T @ x),
    [
        G @ x <= h,
        # A @ x == b
    ]
)
prob.solve()

# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)
print("A dual solution corresponding to the inequality constraints is")
print(prob.constraints[0].dual_value)
