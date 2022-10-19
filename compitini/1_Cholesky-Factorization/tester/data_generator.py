from typing import Tuple
import numpy as np


def __generate_A(size=10, seed=None) -> np.ndarray:
    '''
        Genera una matrice Quadrata, Simmetrica e Definita Positiva di dimensione
        size.
    '''

    # se esplicitamente passato, viene settato il seed
    if seed is not None:
        np.random.seed(seed)

    # magic ✨
    A = np.random.rand(size, size)
    B = np.dot(A, A.transpose())

    return B


def __generate_b(size=10, seed=None) -> np.array:
    '''
        Genera il vettore dei termini noti
    '''

    # se esplicitamente passato, viene settato il seed
    if seed is not None:
        np.random.seed(seed)

    b = np.random.rand(size)

    return b 


def generate_data(size=10, seed=None) -> Tuple[np.ndarray, np.array]:
    '''
        Ritorna una tupla con i dati del sistema lineare A e b.
    '''
    
    return (__generate_A(size, seed), __generate_b(size, seed))