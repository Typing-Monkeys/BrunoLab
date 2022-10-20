from ctypes.wintypes import FLOAT
from math import sqrt
import numpy as np
from numba import jit

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



    '''
    Calcola la fattorizzazione iterando lungo le righe della matrice A

    La variabile trasposed serve perchè se calcolata per righe torna la trasposta di quella calcolata per 
    colonne, quindi così è più facile confrontarle

    '''
    def compute_by_row(A:np.ndarray, transposed:bool) -> np.ndarray:
        
        # Prima di fattorizzare controlla che A rispetta i prerequisiti necessari
        is_factorizable = Cholesky_factorization.__check_requirements(A)

        if not is_factorizable:
            return None
        
        n, _ = A.shape

        L = np.zeros(n*n, dtype=float).reshape(n, n)    # inizializzo la matricce risultato

        for i in range(n):
            for j in range(i, n):
                if (i == j):
                    L[i,j] = np.sqrt(A[i,j]-np.sum(L[:i,j]**2))   # calcolo i valori della diagonale
                else:
                    L[i,j] = (A[i,j]-np.sum(L[:i,j]*L[:i,i])) / L[i,i]   # calcolo i valori delle colonne
        if not transposed:
            return np.round(L, Cholesky_factorization.FLOAT_PRECISION)

        return np.round(L.transpose(), Cholesky_factorization.FLOAT_PRECISION)
        
    def compute_by_row_numba(A:np.ndarray, transposed:bool) -> np.ndarray:
        # Definizione delle robe da fare jit con numba


        # Calcola la fattorizzazione degli elementi lungo la diagonale di A
        @jit(nopython=True)
        def row_diagonal(L:np.ndarray, A:np.ndarray, i:int, j:int) -> bool:
            L[i,j] = np.sqrt(A[i,j]-np.sum(L[:i,j]**2))

        # Calcola la fattorizzazione degli elementi che non sono sulla diagonale di A
        @jit(nopython=True)
        def row_non_diagonal(L:np.ndarray, A:np.ndarray, i:int, j:int) -> bool:
            L[i,j] = (A[i,j]-np.sum(L[:i,j]*L[:i,i])) / L[i,i]


        # Prima di fattorizzare controlla che A rispetta i prerequisiti necessari
        is_factorizable = Cholesky_factorization.__check_requirements(A)

        if not is_factorizable:
            return None
        
        n, _ = A.shape

        L = np.zeros(n*n, dtype=float).reshape(n, n)    # inizializzo la matricce risultato

        for i in range(n):
            for j in range(i, n):
                if (i == j):
                    row_diagonal(L,A,i,j)   # calcolo i valori della diagonale
                else:
                    row_non_diagonal(L,A,i,j)  # calcolo i valori delle colonne


        if not transposed:
            return np.round(L, Cholesky_factorization.FLOAT_PRECISION)

        return np.round(L.transpose(), Cholesky_factorization.FLOAT_PRECISION)
        

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

        L = np.zeros(n*n, dtype=float).reshape(n, n)    # inizializzo la matricce risultato

        for j in range(n):
            for i in range(j, n):
                if (i == j):
                    tmp = 0
                    for k in range((j)):
                        tmp += (L[i][k])**2
                    
                    L[i][j] = sqrt(A[i][j] - tmp)   # calcolo i valori della diagonale

                else:
                    tmp = 0
                    for k in range((j)):
                        tmp += L[i][k] * L[j][k]
                    
                    L[i][j] = (1/L[j][j])*(A[i][j] - tmp)   # calcolo i valori delle colonne

        return np.round(L, Cholesky_factorization.FLOAT_PRECISION)

    def is_correct_solution(A: np.ndarray, L: np.ndarray) -> bool:
        '''
            Applico l'algoritmo implementato in numpy e confronto il risultato con il mio
        '''

        L_correct = np.round(np.linalg.cholesky(A), Cholesky_factorization.FLOAT_PRECISION)

        return (L == L_correct).all() 


def main():
    A = np.array([
        [5.2, 3, 0.5, 1, 2],
        [3, 6.3, -2, 4,0],
        [0.5, -2, 8,-3.1, 3],
        [1, 4, -3.1,7.6,2.6],
        [2,0,3,2.6,15]
    ], dtype=float)

    print(f"A:\n{A}\n")

    L = Cholesky_factorization.compute_by_row_numba(A,1)
    
    if L is None:
        print("Impossibile scomporre la matrice data !!")
        return -1
    
    print(f"L:\n{L}")
    print(f"Il risultato è corretto ?: {'✅' if (Cholesky_factorization.is_correct_solution(A, L)) else '❌'}")


if __name__ == "__main__":
    main()
