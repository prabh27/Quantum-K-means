from sympy.solvers import solve
from sympy import Symbol, I
import numpy as np
import sympy
from sympy.physics.quantum.dagger import Dagger
import csv

b = sympy.symarray('b', 41)
alpha = sp.Symbol('alpha')

U = sympy.Matrix([
        [1/3, 2/3, 2/3, 1/3, 2/3, 1/3, b[1], b[2]],
        [1/2, 2/2, 0,   1/2,  0,  1,   b[3], b[4]],
        [1/2, 0,   2/2,  1,   0,  1/2, b[5], b[6]],
        [1,   0,    0,  1/2, 2/2, 1/2, b[7], b[8]],
        b[9:17],
        b[17:25],
        b[25:33],
        b[33:41]
])
U = U/alpha

mul = Dagger(U) * U

I = sympy.eye(8)

ans = solve(mul - I, dict=True)

with open('unitary_matrix_3_datapoints.csv', 'w') as f:
    for i in range(len(ans)):
        for key in ans[i].keys():
            f.write("%s,%s\n"%(key,ans[i][key]))