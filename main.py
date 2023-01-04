# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import mapping
import numpy as np


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = mapping.mapping(3, 4, np.array([[1,0,0,0], [0,0,1,0], [0,0,0,1]]))
    print(a(0), a(1), a(2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
