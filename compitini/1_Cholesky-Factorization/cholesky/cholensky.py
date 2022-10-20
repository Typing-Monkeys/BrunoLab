from ctypes.wintypes import FLOAT
from math import sqrt
from numba import jit
import numpy as np


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


def compute_columns_no_numba(A: np.ndarray) -> np.ndarray:
    '''
        Applica la fattorizzazinoe di Cholesky per ottenere la matrice L
        Per poter funzionare devono essere rispettate le condizioni imposte dalle
        precedenti funzioni.
    '''

    is_factorizable = __check_requirements(A)

    # i vincoli non sono soddisfatti, la matrice data non si può fattorizzare
    if not is_factorizable:
        return None

    n, _ = A.shape

    L = np.zeros(n*n, dtype=float).reshape(n, n)    # inizializzo la matricce risultato

    for j in range(n):
        for i in range(j, n):
            if (i == j):
                L[i,j] = np.sqrt(A[i,j]-np.sum(L[i,:j]**2))   # calcolo i valori della diagonale
            else:
                L[i,j] = (A[i,j]-np.sum(L[i,:j]*L[j,:j])) / L[j,j]   # calcolo i valori delle colonne

    return L

def compute(A: np.ndarray) -> np.ndarray:
    '''
        Applica la fattorizzazinoe di Cholesky per ottenere la matrice L
        Per poter funzionare devono essere rispettate le condizioni imposte dalle
        precedenti funzioni.
    '''
    #TODO: Vedere se definirle qui dentro peggiora il tempo di esecuzione (forse le deve ricompilare ogni volta?)
    @jit(nopython=True)
    def column_columns_numba(L: np.array,A: np.array,i: int,j: int) -> bool:
        L[i,j] = np.sqrt(A[i,j]-np.sum(L[i,:j]**2))

    @jit(nopython=True)
    def row_columns_numba(L: np.array,A: np.array,i: int,j: int) -> bool:
        L[i,j] = (A[i,j]-np.sum(L[i,:j]*L[j,:j])) / L[j,j]
    
    is_factorizable = __check_requirements(A)

    # i vincoli non sono soddisfatti, la matrice data non si può fattorizzare
    if not is_factorizable:
        return None

    n, _ = A.shape

    L = np.zeros(n*n, dtype=float).reshape(n, n)    # inizializzo la matricce risultato

    for j in range(n):
        for i in range(j, n):
            if (i == j):
                column_columns_numba(L,A,i,j)   # calcolo i valori della diagonale
            else:
                row_columns_numba(L,A,i,j)   # calcolo i valori delle colonne

    return L



def is_correct_solution(A: np.ndarray, L: np.ndarray) -> bool:
		'''
            Controllo che la soluzione sia corretta ricalcolando A da LS
		'''

		A_bis = np.dot(L, np.transpose(L))
		
        # print(A_bis)

		return np.allclose(A, A_bis, 0.001)
