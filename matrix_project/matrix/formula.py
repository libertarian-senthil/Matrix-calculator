# Status:active
# All the other formulas are done here

import numpy as np
from mat_input import *

class formula:
    """ Preforms matrix oriented operations """
    
    def __init__(self, arr_a = None, arr_b = None):    # Constructor
        self.arr_a= np.array(arr_a)
        self.arr_b= np.array(arr_b)
        self.result= None
        
    def  square(self, dim):
        """ Returns Square of two arrays of same dimension """
        self.arr_a= matrix(dim, dim)
        self.result= np.square(self.arr_a)
        return self.result
    
    def trans(self, dim): 
        """ Returns Transpose of two arrays of same dimension """
        self.arr_a= matrix(dim, dim) 
        self.result= np.transpose(self.arr_a)
        return self.result

if __name__ == '__main__':
    a= formula()
    print(a.square(2))
    print(a.transpose(2))

#yet to be completed
