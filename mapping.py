import numpy as np

class mapping:
    def __init__(self, domain_ord: int, codomain_ord: int, mapping_table: np.array):
        """
        We initialize a mapping with the orders of domain and codomain sets and mapping table
        """
        if domain_ord != mapping_table.shape[0] or codomain_ord != mapping_table.shape[1] or mapping_table.ndim != 2:
            print('It\'s not a mapping')
            return
        for row in mapping_table:
            if np.count_nonzero(row) != 1 or 1 not in row:
                print('It\'s not a mapping')
                return
        self.domain_ord = domain_ord
        self.codomain_ord = codomain_ord
        self.mapping_table = mapping_table

    def __call__(self, x: int) -> int:
        '''
        Returns the value of the mapping on an argument
        '''
        try:
            return np.where(self.mapping_table[x] == 1)[0][0]
        except IndexError:
            print('Out of the domain set')
            return None
