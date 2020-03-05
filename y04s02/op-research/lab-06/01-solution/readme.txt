Operation Research Lab 06

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

Variant 28

1 x_1 + 1 x_2 <= 15
2 x_1 + 5 x_2 <= 60
3 x_1 + 1 x_2 <= 30

x_1, x_2 >= 0

z = x_1^2 + x_2^2 - 18 x_1 - 20 x_2 → min.
