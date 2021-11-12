#Status: active

import numpy as np
 
def matrix(row, column):
    '''
    Create a matrix with the given row and column

    Parameters
    ----------
    row : int
        This parameter is used for creating row of a matrix.
    column : int
        This parameter is used for creating column of a matrix.
    
    Return
    ------
        Returns the matrix created 
    '''

    while True:
        emp_arr = np.zeros((row, column), dtype=np.int64)
        try:
            for i in range(row):
                for j in range(column):
                    e = input(f"a[{i}][{j}]: ")
                    if e == "quit":
                        print("Process Stopped: Exited")
                        return ""
                    else:
                        emp_arr[i][j] = int(e)
            return emp_arr
        except ValueError:
            print("You've given a incorrect input")


# Drive code
if __name__ == '__main__':
    print(matrix(1, 2))
