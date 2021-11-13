# Status: active

import numpy as np

def matrix(row, column):
    """
    Creates a matrix with given row and column 

    Parameters
    ----------
    row : int
        This parameter is used for creating row of a matrix.
    column : int
        This parameter is used for creating column of a matrix.
    
    Return
    ------
        Returns the matrix created 
    """

    arr = np.zeros((row, column), dtype= np.int64)
    i = 0

    while i < row:
        j = 0
        while j < column:
            element = input(f"a[{i}][{j}]: ").lower()
            if element == "quit":
                print("Process Stopped: Exited")
                return ""
            else:
                try:
                    int(element)
                except ValueError:
                    print("Invalid input enter again or enter quit to exit.")
                    continue
                else:
                    arr[i][j] = element

            j+= 1
        i+= 1
    return arr

if __name__ == "__main__":
    print(matrix(2, 3))
