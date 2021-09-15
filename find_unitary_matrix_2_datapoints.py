from sympy.solvers import solve
from sympy import Symbol, I
import numpy as np
import sympy as sp
from sympy.physics.quantum.dagger import Dagger
import csv

r1 = Symbol('r1')
r2 = Symbol('r2')
r3 = Symbol('r3')
r4 = Symbol('r4')
r5 = Symbol('r5')
r6 = Symbol('r6')
r7 = Symbol('r7')
r8 = Symbol('r8')
r9 = Symbol('r9')
r10 = Symbol('r10')
alpha = sp.Symbol('alpha')

U = sp.Matrix([
        [0.5,           1,    0.5,      r1],
        [1,             0,     1,       r2],
        [0.5,           1,     r5,      r6],
        [r1,            r2,    r6,      r10]
])

U = U/alpha

mul = Dagger(U) * U
I = sp.eye(4)

ans = solve(mul - I, dict=True)

with open('unitary_matrix_2_datapoints.csv', 'w') as f:
    for key in ans[0].keys():
        f.write("%s,%s\n"%(key,ans[0][key]))

