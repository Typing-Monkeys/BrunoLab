from typing import Tuple
import tester as Tester
import cholesky as Cholesky_factorization
import linsys as Linear_sistem
import numpy as np


def solve(A: np.ndarray, b: np.array, method="column", jit=False, verbose=True) -> Tuple[np.array, Tuple[int, int]]:
    '''
        Risolve un dato Sistema Lineare con la fattorizzazione di Cholesky.

        inputs:
            A:          matrice che rappresenta il Sistema
            b:          vettore dei termini noti
            verobse:    se False, non stampa a schermo nulla

        returns:
            Tuple(
                x -> soluzione del sistema
                Tuple (
                    c,  -> tempo (in ms) impiegato per risolvere Cholesky
                    l   -> tempo (in ms) impiegato per risolvere il Sistema
                )
            )
    '''
    
    logger = Tester.Logger(verbose)

    # --- Visualizzo i dati iniziali --- #
    logger.print(f"A:\n{A}\n")
    logger.print(f"b:\n{b}\n")

    # --- Decomposizione della matrice A in LU --- #
    logger.print("CHOLESKY FACTORIZATION ...")

    cholesky_execution_time, L = Tester.get_execution_time(Cholesky_factorization.compute, [A, method, jit])
    
    if L is None:
        logger.print("Impossibile scomporre la matrice data !!", force=True)
        return -1
    
    logger.print(f"L:\n{L}\n")
    logger.print(f"Il risultato è corretto ?: {'✅' if (Cholesky_factorization.is_correct_solution(A, L)) else '❌'}")
    logger.print(f"Tempo di esecuzione: {cholesky_execution_time}")
    logger.print('\n')

    # --- Risoluzione del Sistema Lineare --- #
    logger.print("SOLVING LINEAR SYSTEM ...")

    linsys_execution_time, x = Tester.get_execution_time(Linear_sistem.solve, [L, b])

    logger.print(f"x: \n{x}\n")
    logger.print(f"Il risultato è corretto ?: {'✅' if (Linear_sistem.is_correct_solution(A, x, b)) else '❌'}")
    logger.print(f"Tempo di esecuzione: {linsys_execution_time}")

    return (x, (cholesky_execution_time, linsys_execution_time))


def find_limit(starting_size=100, seed=20, method="column", jit=False):
    size = starting_size
    while True:
        print(f"SIZE: {size}x{size}")

        A, b = Tester.generate_data(size, seed)
        _, execution_times = solve(A, b, method, jit, verbose=False)
        
        print(f"Cholesky Execution Time: {execution_times[0]} ms")
        print(f"Linear System Execution Time: {execution_times[1]} ms")
        print(f"Total Execution Time: {sum(execution_times)} ms")
        print("\n")
        
        size *= 2