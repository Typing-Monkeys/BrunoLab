class Logger:
    def __init__(self, verbose=True):
        self.verbose = verbose

    def print(self, output: str, force=False):
        '''
            Stampa l'output dato solo se verbose è True.

            Se force è True, forza la stampa indipendentemente da verbose.
        '''

        if self.verbose or force:
            print(output)