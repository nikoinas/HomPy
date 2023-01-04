from mapping import mapping
import numpy as np

class group:

    def __init__(self, order: int, cayley_table: np.array):
        """
        """
        if order != cayley_table.shape[0] or order != cayley_table.shape[1] or cayley_table.ndim != 2:
            print('It\'s not an operation')
            return
        self.order = order
        self.cayley_table = cayley_table

class homomorphism(mapping):

    def __init__(self, domain_ord: int, domain_table: np.array, codomain_ord: int, codomain_table: np.array,
                 mapping_table: np.array):
        """
        """
        super().__init__(domain_ord, codomain_ord, mapping_table)

        self.domain_table = domain_table
        self.codomain_table = codomain_table
