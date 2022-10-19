import tester as Tester
import argparse


def main(args):
    if args.find_limit:
        Tester.find_limit(seed=20)

    else:
        A, b = Tester.generate_data(size=5, seed=20)

        _ = Tester.solve(A, b)

    """ A = np.array([
        [5.2, 3, 0.5, 1, 2],
        [3, 6.3, -2, 4,0],
        [0.5, -2, 8,-3.1, 3],
        [1, 4, -3.1,7.6,2.6],
        [2,0,3,2.6,15]
    ], dtype=float)

    b = np.array([9.45, -12.20, 7.78, -8.1, 10.0], dtype=float) # termine noto 
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--find_limit", 
        action="store_true",
        help="Avvia la procedura per testare la velocità di risoluzione con matrici di grandezza crescente"
    )

    args = parser.parse_args()

    main(args)
