import numpy as np


def solve(L, b):

    '''
        Solve linear sistem using cholesky decomposition 
        with matrix L
        
        L -> Decomposition matrix by cholesky ( lower triangular matrix ) 
        U -> Upper triangular matrix 
        b -> Know term 
        x,y -> The solutio of equation
        x -> The solution using Backword subsostitution
        y -> The solution using Forword sostitution
        
        a_11 a12 ... a_1n  x_1      b1
        a_12 a22 ... a_2n  x_2      b2
        ...  ... ... ...         =  ...
        a_n1 an2 ... a_nn  x_n      bn 
        
        linear system --->   [a] {x} = {b}
        
        1. Decomposition: [a] = [L][U]
        2. Substitution: [L][U] = {b}
            2.1 Backword substitution [U]{x} = {y}
            2.2 Forward substitution [L]{y} = {b}         
    '''

    # Transformation the matrix by 0 and shape
    L = np.array(L, float)
    U = np.transpose(L)
    b = np.array(b, float)
    n, _ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)

    # Forword sostitution
    for i in range(n):
        sumj = 0
        for j in range(i):
            sumj += L[i, j] * y[j]

        y[i] = (b[i]-sumj)/L[i, i]

    # Backword subsostitution
    for i in range(n-1, -1, -1):
        sumj = 0
        for j in range(i+1, n):
            sumj += U[i, j] * x[j]

        x[i] = (y[i]-sumj)/U[i, i]

    return x


def check_solution(A: np.ndarray, x: np.array, b: np.array) -> bool:
    '''
        Controlla che la soluzione x al sistema dato Ab sia corretta.
        Questo viene fatto moltiplicando A per x e controllando che il risultato sia
        uguale a b
               
               ??
            Ax == b
    '''

    b_bis = A.dot(x)

    return np.allclose(b, b_bis, 0.01)
