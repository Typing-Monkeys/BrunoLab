from typing import Any, Callable, Tuple
from .execution_time import get_execution_time
from .data_generator import generate_data
import cholesky as Cholesky_factorization
import gauss as Gaussian_elimination
import linsys as Linear_sistem
import numpy as np


ALGORITHM = "cholesky"


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
    
    # print(f"fun: {ALGORITHM}")

    def cholesky():
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

    def gauss():
        Ab = np.c_[A, b]    # Augmented Matrix

        # --- Visualizzo i dati iniziali --- #
        print(f"A:\n{A}\n")
        print(f"b:\n{b}\n")
        print(f"Ab:\n{Ab}\n")

        # --- Applicazione dell'algoritmo di eliminaizone di Gauss --- #
        print("GAUSSIAN ELIMINATION ...")

        gauss_execution_time, U = get_execution_time(Gaussian_elimination.compute, [Ab])
        
        if U is None:
            print("Impossibile applicare l'algoritmo di Gauss sualla matrice data !!")
            return -1
        
        print(f"U:\n{U}\n")
        print(f"Il risultato è corretto ?: {'✅' if (Gaussian_elimination.is_correct_solution(A, U, b)) else '❌'}")
        print(f"Tempo di esecuzione: {gauss_execution_time}")
        print('\n')

        # --- Risoluzione del Sistema Lineare --- #
        print("SOLVING LINEAR SYSTEM ...")

        linsys_execution_time, x = get_execution_time(Linear_sistem.solve, [None, U, None])

        print(f"x: \n{x}\n")
        print(f"Il risultato è corretto ?: {'✅' if (Linear_sistem.is_correct_solution(A, x, b)) else '❌'}")
        print(f"Tempo di esecuzione: {linsys_execution_time}")

        return (x, (gauss_execution_time, linsys_execution_time))


    match ALGORITHM:
        case "cholesky":
            return cholesky()
        case "gauss":
            return gauss()
        case _:
            raise Exception("Bad Algorithm Name !")


def find_limit(starting_size=100, seed=20, method="column", jit=False):
    size = starting_size
    
    while True:
        print(f"SIZE: {size}x{size}")

        A, b = generate_data(size, seed)

        execution_time, _ =  get_execution_time(Cholesky_factorization.compute, [A, method, jit])
        
        print(f"Cholesky Execution Time: {execution_time} ms")
        print("\n")
        
        size *= 2


# TODO: implementare !
#       questa funzione deve prendere in input un algoritmo (Gauss o Cholesky)
#       e testarlo su una data matrice per vedere quanto è veloce.
def benchmark(algorithm: Callable) -> Tuple[int, Any]:
    raise NotImplementedError


def set_algorithm(string: str):
    '''
        Cambia l'algoritmo da utilizzare

            Cholesky/Gauss
    '''
    global ALGORITHM

    ALGORITHM = string