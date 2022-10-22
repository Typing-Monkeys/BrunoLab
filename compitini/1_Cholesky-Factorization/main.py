import tester as Tester
import argparse


def main(args):
    # questo funziona solo da python 3.10 in poi
    # TODO: ci piace ??
    match args.test_mode:
        case "find_limit":
            Tester.find_limit(seed=args.seed, method=args.method, jit=args.jit)

        case "simple":
            A, b = Tester.generate_data(size=args.size, seed=args.seed)

            _ = Tester.simple_test(A, b, method=args.method, jit=args.jit)
        
        case _:
            return -1
    
    """ if args.test_mode == "find_limit":
        Tester.find_limit(seed=args.seed, method=args.method, jit=args.jit)

    elif args.test_mode == "simple":
        A, b = Tester.generate_data(size=5, seed=args.seed)

        _ = Tester.simple_test(A, b, method=args.method, jit=args.jit)

    else:
        return -1
     """
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
        "-tm",
        "--test_mode", 
        type=str,
        choices=["simple", "find_limit"],
        default="simple",
        help="Avvia una tra le varie procedure di testing."
    )

    parser.add_argument(
        "-m",
        "--method", 
        type=str,
        choices=["row", "column", "diagonal"],
        default="column",
        help="Indica l'implementazione di Cholesky da utilizzare."
    )

    parser.add_argument(
        "--jit", 
        action="store_true",
        help="Utilizza la JIT Compile per migliorare le performance."
    )

    parser.add_argument(
        "--seed", 
        type=int,
        default=20,
        help="Specifica il seed per la ripetibilità dei test."
    )

    parser.add_argument(
        "--size", 
        type=int,
        default=5,
        help="Specifica la dimensione della matrice (se possibile)."
    )

    args = parser.parse_args()

    main(args)
