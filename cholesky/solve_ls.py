from ctypes.wintypes import FLOAT
from math import sqrt
import numpy as np


class Cholesky_factorization:
    FLOAT_PRECISION = 2

    def __check_requirements(A: np.ndarray) -> bool:

        def is_square(matrix: np.ndarray) -> bool:
            '''
                Questa funzione controlla che la matrice data sa Quadrata:
                    A = nxn
            '''

            n, m = matrix.shape

            if(m == n):
                return True

            return False

        def is_symmetric(matrix: np.ndarray) -> bool:
            '''
                Questa funzione controlla che la matrice si Simmetrica:
                    a_ij = a_ji     (deve essere simmetrica sulla diagonale)
                        oppure
                    At = A          (la trasposta è uguale a se stessa)
            '''

            if(np.allclose(matrix.transpose(), matrix)):
                return True

            return False

        def is_positive_definite(matrix: np.ndarray) -> bool:
            '''
                Questa funzione controlla che la matrice sia Definita Positiva:
                    eigenvalues > 0     (tutti gli eigenvalue della matrice devono essere positivi)
            '''

            eigenvals = np.linalg.eigvals(matrix)

            if (np.all(eigenvals > 0)):
                return True

            return False

        # controlla se tutti i requisiti sono soddisfatti
        return is_square(A) and is_symmetric(A) and is_positive_definite(A)

    def compute(A: np.ndarray) -> np.ndarray:
        '''
            Applica la fattorizzazinoe di Cholesky per ottenere la matrice L
            Per poter funzionare devono essere rispettate le condizioni imposte dalle
            precedenti funzioni.
        '''

        is_factorizable = Cholesky_factorization.__check_requirements(A)

        # i vincoli non sono soddisfatti, la matrice data non si può fattorizzare
        if not is_factorizable:
            return None

        n, _ = A.shape

        # inizializzo la matricce risultato
        L = np.zeros(n*n, dtype=float).reshape(n, n)

        for j in range(n):
            for i in range(j, n):
                if (i == j):
                    tmp = 0
                    for k in range((j)):
                        tmp += (L[i][k])**2

                    # calcolo i valori della diagonale
                    L[i][j] = sqrt(A[i][j] - tmp)

                else:
                    tmp = 0
                    for k in range((j)):
                        tmp += L[i][k] * L[j][k]

                    # calcolo i valori delle colonne
                    L[i][j] = (1/L[j][j])*(A[i][j] - tmp)

        return np.round(L, Cholesky_factorization.FLOAT_PRECISION)

    def is_correct_solution(A: np.ndarray, L: np.ndarray) -> bool:
        '''
            Applico l'algoritmo implementato in numpy e confronto il risultato con il mio
        '''

        L_correct = np.round(np.linalg.cholesky(
            A), Cholesky_factorization.FLOAT_PRECISION)

        return (L == L_correct).all()

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

    def solveLU(L, U, b):

        # Transformation the matrix by 0 and shape
        L = np.array(L, float)
        U = np.array(U, float)
        b = np.array(b, float)
        n, _ = np.shape(L)
        y = np.zeros(n)
        x = np.zeros(n)

        # Add 1 column to matrix for compose complet matrix 
        ux_matrix = np.append(U, b, axis=1)

        print("\n Complet Matrix")
        print(ux_matrix)

        n = len(x)

        # Calcolate element to diagonal U matrix 
        diagon_u = U.diagonal()

        # Calcolate element to diagonal UX matrix 
        diagon_ux = ux_matrix.diagonal()
        
        # Calcolate len diagonal U 
        det_u = len(diagon_u)

        # Calolcate len diagonal UX
        det_ux = len(diagon_ux)

        '''
            Rouche Capelli Theorem 

            1. Solution:

                The Rouché-Capelli theorem states that solutions exist for the system 
                
                IF AND ONLY IF 
                
                the rank of the complete matrix IS EQUAL to the rank of the incomplete matrix
            
            2. NO SOLUTION: 

                IF the rank of the incomplete matrix IS LOWER to the rank of complete matrix 
        '''

        if det_u == det_ux:
            
            print("\n")

            print(f"Det of first matrix: {det_u}")

            print("\n")

            print(f"Det of second matrix: {det_ux}")

            print("\n")

            print("The system is solvable")

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

        else:
            print("Linear system is not solvable")
    
def main():
    A = np.array([
        [5.2, 3, 0.5, 1, 2],
        [3, 6.3, -2, 4, 0],
        [0.5, -2, 8, -3.1, 3],
        [1, 4, -3.1, 7.6, 2.6],
        [2, 0, 3, 2.6, 15]
    ], dtype=float)

    print(f"A:\n{A}\n")

    L = Cholesky_factorization.compute(A)

    if L is None:
        print("Impossibile scomporre la matrice data !!")
        return -1

    print(f"L:\n{L}")
    print(
        f"Il risultato è corretto ?: {'✅' if (Cholesky_factorization.is_correct_solution(A, L)) else '❌'}")

    # Known term
    B = np.array([[9.45], 
                  [-12.20], 
                  [7.78], 
                  [-8.1], 
                  [10.0]])

    print("\n")

    print("\t\t\tLower matrix")

    # Lower matrix create
    print(L)

    print("\n")

    print("\t\t\tTranspose matrix")

    # Upper matrix
    U = np.transpose(L)
    print(U)

    '''
        Solve system using Backword subsostitution
        l -> Lower matrix 
        u -> Upper matrix 
        b -> Know term 
    '''
    x = Cholesky_factorization.solveLU(L, U, B)

    print("\n")

    print("\tSolve linear system with cholesky and backword sostitution")
    print(x)

    print("\n")

    print("\t\tSolve linear system using a np.linalg method")
    # Solve system using a np.linalg method
    x2 = np.linalg.solve(A, B)

    print(x2)

 


if __name__ == "__main__":
    main()