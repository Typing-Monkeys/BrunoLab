import numpy as np
import cholesky as Cholesky_factorization
import linsys as Linear_sistem
import tester as Tester


def main():
    A, b = Tester.generate_data(size=5, seed=20)

    """ A = np.array([
        [5.2, 3, 0.5, 1, 2],
        [3, 6.3, -2, 4,0],
        [0.5, -2, 8,-3.1, 3],
        [1, 4, -3.1,7.6,2.6],
        [2,0,3,2.6,15]
    ], dtype=float)

    b = np.array([9.45, -12.20, 7.78, -8.1, 10.0], dtype=float) # termine noto """

    print(f"A:\n{A}\n")
    print(f"b:\n{b}\n")

    # --- Decomposizione della matrice A in LU --- #
    print("CHOLESKY FACTORIZATION ...")

    execution_time, L = Tester.get_execution_time(Cholesky_factorization.compute, [A])
    
    if L is None:
        print("Impossibile scomporre la matrice data !!")
        return -1
    
    print(f"L:\n{L}\n")
    print(f"Il risultato è corretto ?: {'✅' if (Cholesky_factorization.is_correct_solution(A, L)) else '❌'}")
    print(f"Tempo di esecuzione: {execution_time}")
    print('\n')

    # --- Risoluzione del Sistema Lineare --- #
    print("SOLVING LINEAR SYSTEM ...")

    execution_time, x = Tester.get_execution_time(Linear_sistem.solve, [L, b])

    print(f"x: \n{x}\n")
    print(f"Il risultato è corretto ?: {'✅' if (Linear_sistem.is_correct_solution(A, x, b)) else '❌'}")
    print(f"Tempo di esecuzione: {execution_time}")


if __name__ == "__main__":
    main()
