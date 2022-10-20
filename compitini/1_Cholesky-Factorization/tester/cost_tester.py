from typing import Tuple
from .execution_time import get_execution_time
from .data_generator import generate_data
import cholesky as Cholesky_factorization
import linsys as Linear_sistem
import numpy as np


def simple_test(A: np.ndarray, b: np.array, method="column", jit=False) -> Tuple[np.array, Tuple[int, int]]:
    '''
        Risolve un dato Sistema Lineare con la fattorizzazione di Cholesky.

        inputs:
            A:          matrice che rappresenta il Sistema
            b:          vettore dei termini noti
            jit:        applica la JIT per migliorare le performance di Cholesky

        returns:
            Tuple(
                x -> soluzione del sistema
                Tuple (
                    c,  -> tempo (in ms) impiegato per risolvere Cholesky
                    l   -> tempo (in ms) impiegato per risolvere il Sistema
                )
            )
    '''
    
    # --- Visualizzo i dati iniziali --- #
    print(f"A:\n{A}\n")
    print(f"b:\n{b}\n")

    # --- Decomposizione della matrice A in LU --- #
    print("CHOLESKY FACTORIZATION ...")

    cholesky_execution_time, L = get_execution_time(Cholesky_factorization.compute, [A, method, jit])
    
    if L is None:
        print("Impossibile scomporre la matrice data !!", force=True)
        return -1
    
    print(f"L:\n{L}\n")
    print(f"Il risultato è corretto ?: {'✅' if (Cholesky_factorization.is_correct_solution(A, L)) else '❌'}")
    print(f"Tempo di esecuzione: {cholesky_execution_time}")
    print('\n')

    # --- Risoluzione del Sistema Lineare --- #
    print("SOLVING LINEAR SYSTEM ...")

    linsys_execution_time, x = get_execution_time(Linear_sistem.solve, [L, b])

    print(f"x: \n{x}\n")
    print(f"Il risultato è corretto ?: {'✅' if (Linear_sistem.is_correct_solution(A, x, b)) else '❌'}")
    print(f"Tempo di esecuzione: {linsys_execution_time}")

    return (x, (cholesky_execution_time, linsys_execution_time))


def find_limit(starting_size=100, seed=20, method="column", jit=False):
    size = starting_size
    
    while True:
        print(f"SIZE: {size}x{size}")

        A, b = generate_data(size, seed)

        execution_time, _ =  get_execution_time(Cholesky_factorization.compute, [A, method, jit])
        
        print(f"Cholesky Execution Time: {execution_time} ms")
        print("\n")
        
        size *= 2
