import tester as Tester
import argparse


def main(args):
    # questo funziona solo da python 3.10 in poi
    # TODO: ci piace ??
    match args.test_mode:
        case "find_limit":
            Tester.find_limit(seed=args.seed, method=args.method, jit=args.jit)

        case "simple":
            Tester.set_algorithm(args.algorithm)
            _ = Tester.simple_test(
                    size=args.size, 
                    seed=args.seed, 
                    method=args.method, 
                    jit=args.jit
                )
        
        case _:
            return -1


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

    parser.add_argument(
        "-alg",
        "--algorithm", 
        type=str,
        choices=["cholesky", "gauss"],
        default="cholesky",
        help="Indica quale tra i possibili algoritmi utilizzare."
    )

    args = parser.parse_args()

    main(args)
