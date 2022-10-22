from ctypes.wintypes import FLOAT
from math import sqrt
import numpy as np

class Cholesky_factorization:
	FLOAT_PRECISION = 2

	def __check_requirements(A: np.ndarray) -> bool:

		def is_square(matrix: np.ndarray) -> bool:
			'''
			returns:
				controlla che la matrice data sia Quadrata:
					A = nxn
			'''
			n, m = matrix.shape

			if(m == n):
				return True
			
			return False


		def is_symmetric(matrix: np.ndarray) -> bool:
			'''
			returns:
				controlla che la matrice sia Simmetrica:
					a_ij = a_ji     (deve essere simmetrica sulla diagonale)
						oppure
					At = A          (la trasposta è uguale a se stessa)
			'''
			if(np.allclose(matrix.transpose(), matrix)):
				return True
			
			return False


		def is_positive_definite(matrix: np.ndarray) -> bool:
			'''
			returns:
				controlla che la matrice sia Definita Positiva:
					eigenvalues > 0     (tutti gli eigenvalue della matrice devono essere positivi)
			'''
			eigenvals = np.linalg.eigvals(matrix)

			if (np.all(eigenvals > 0)):
				return True

			return False

		# controlla se tutti i requisiti sono soddisfatti
		return is_square(A) and is_symmetric(A) and is_positive_definite(A)


	def compute(A: np.ndarray) -> np.ndarray:
		def cholesky_formula(i, j, A, L):
			to_return = 0
			if (i == j):
				tmp = 0
				for k in range((j)):
					tmp += (L[i][k])**2
				
				to_return = sqrt(A[i][j] - tmp)   # calcolo i valori della diagonale

			else:
				tmp = 0
				for k in range((j)):
					tmp += L[i][k] * L[j][k]
				
				to_return = (1/L[j][j])*(A[i][j] - tmp)   # calcolo i valori delle colonne
			
			return to_return


		is_factorizable = Cholesky_factorization.__check_requirements(A)

		# i vincoli non sono soddisfatti, la matrice data non si può fattorizzare
		if not is_factorizable:
			return None

		n, _ = A.shape

		L = np.zeros(n*n, dtype=float).reshape(n, n)    # inizializzo la matricce risultato

		external = 0 #variabile per contare quanti cicli esterni devo fare
		internal = 2 * n - 1 - 1

		aux = 0
		for row in range(2 * n - 1):
			if row < n-1:
				col = 0
				L[row, col] = cholesky_formula(row, col, A, L)
				aux += 1
				for z in range(1, int(np.floor(row/2))+1):
					L[row-z, col+z] = cholesky_formula(row-z, col+z, A, L)

			else:
				col = n-1
				L[col, row-aux] = cholesky_formula(col, row-aux, A, L)
				for z in range(1, int(np.floor(internal/2))+1):
					L[col-z, row-aux+z] = cholesky_formula(col-z, row-aux+z, A, L)

			internal -= 1   
			external += 1
			

		return np.round(L, Cholesky_factorization.FLOAT_PRECISION)

	
	def is_correct_solution_vescers(A: np.ndarray, L: np.ndarray) -> bool:
		'''
			returns:
				confronto che il risultato della mia funzione sia corretto
				rispetto alla funzione di numpy
		'''
		L_correct = np.round(np.linalg.cholesky(A), Cholesky_factorization.FLOAT_PRECISION)

		return (L == L_correct).all()
	

	def is_correct_solution(A: np.ndarray, L: np.ndarray) -> bool: #controllo che la soluzione sia corretta ricalcolando A da L
		'''
			returns:
				confronto che il risultato della mia funzione sia corretto
				riottenendo la matrice originale A da L
		'''
		A_bis = np.round(np.dot(L, np.transpose(L)), Cholesky_factorization.FLOAT_PRECISION-1)
		print(A_bis)

		return (A_bis == A).all()


def generate_A(size=10, seed=69) -> np.ndarray:
    '''
        Genera una matrice Quadrata, Simmetrica e Definita Positiva di dimensione
        size.
    '''

    # magic ✨
    A = np.random.rand(size, size)
    B = np.dot(A, A.transpose())

    return B


def main():
	A = generate_A(100)

	'''
	A = np.array([
		[5.2, 3, 0.5, 1, 2],
		[3, 6.3, -2, 4,0],
		[0.5, -2, 8,-3.1, 3],
		[1, 4, -3.1,7.6,2.6],
		[2,0,3,2.6,15]
	], dtype=float)
	'''

	print(f"A:\n{A}\n")

	L = Cholesky_factorization.compute(A)
	
	if L is None:
		print("Impossibile scomporre la matrice data !!")
		return -1
	
	print(f"L:\n{L}")
	print(f"Il risultato è corretto ?: {'✅' if (Cholesky_factorization.is_correct_solution_vescers(A, L)) else '❌'}")


if __name__ == "__main__":
	main()
