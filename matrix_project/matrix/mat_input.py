#Status: active
#Basic matrix input file for all arithmetic values
# This module is currently being halted from develpment so, don't improve or develop the contents of this particular module

import numpy as np
# from matrix import arithmetic 
def matrix(row, column):
    ''' matrix addition'''
    while True:
        emp_arr = np.zeros((row, column), dtype=np.int64)
        try:
            for i in range(row):
                for j in range(column):
                    e = int(input(f"a[{i}][{j}]: "))
                    emp_arr[i][j] = e
            return emp_arr
        except ValueError:
            print("You've given a incorrect input")


# Drive code
if __name__ == '__main__':
    print(matrix(1, 2))
