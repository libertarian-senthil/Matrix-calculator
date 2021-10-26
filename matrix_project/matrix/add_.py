# Status: not-active
# Addition module 
# This module is currently being halted from develpment so, don't improve or develop the contents of this particular module


import numpy as np

def add(a,b):
    try:
        emp_arr= np.add(a, b)
        print(emp_arr, type(emp_arr), sep= "\n")
        return
    except ValueError:
        print(f"invalid dimensions ({a.shape}) ({b.shape})")

# Drive code
if __name__ == '__main__':
    a= np.array([[1, 1], 
        [2, 2], 
        [3, 3]])

    b= np.array([[1, 1, 1], 
        [2, 2, 2], 
        [3, 3, 3]])
    add(a,b)
#yet to be completed
