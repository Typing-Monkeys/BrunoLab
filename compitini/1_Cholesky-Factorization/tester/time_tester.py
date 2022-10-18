from time import time
from typing import Any, Callable, Tuple
import numpy as np


def __get_time(millis=True) -> int:
    actual_time = round(time())
    return (actual_time * 1000) if millis else actual_time


def get_execution_time(function: Callable, parameters=[]) -> Tuple[int, Any]:
    start_time = __get_time() # in millisecondi

    result = function(*parameters)

    end_time = __get_time()

    execution_time = end_time - start_time

    return (execution_time, result)


def generate_matrix(size=10, seed=None) -> np.ndarray:
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


if __name__ == "__main__":
    from time import sleep
    
    matrix = generate_matrix(4)
    print(matrix)

    def test(a, b):
        print(f"a: {a}; b: {b}")
        sleep(10)
        return 100

    execution_time, result = get_execution_time(test, [1, 2])

    print(execution_time, result)