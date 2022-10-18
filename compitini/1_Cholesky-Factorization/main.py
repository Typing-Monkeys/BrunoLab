import cholesky as Cholesky_factorization
import numpy as np


def main():
    A = np.array([
        [5.2, 3, 0.5, 1, 2],
        [3, 6.3, -2, 4,0],
        [0.5, -2, 8,-3.1, 3],
        [1, 4, -3.1,7.6,2.6],
        [2,0,3,2.6,15]
    ], dtype=float)

    print(f"A:\n{A}\n")

    L = Cholesky_factorization.compute(A)
    
    if L is None:
        print("Impossibile scomporre la matrice data !!")
        return -1
    
    print(f"L:\n{L}")
    print(f"Il risultato è corretto ?: {'✅' if (Cholesky_factorization.is_correct_solution(A, L)) else '❌'}")


if __name__ == "__main__":
    main()