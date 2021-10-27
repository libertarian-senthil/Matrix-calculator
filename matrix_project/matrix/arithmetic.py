# Status: active
# All the matrices calculations are done here.

import numpy as np
from mat_input import *

class arithmetic:
    """ Class returns the arithmetic operations for matrices """
    
    def __init__(self, arr_a= None, arr_b= None): # Constructor
        self.arr_a= np.array(arr_a)
        self.arr_b= np.array(arr_b)
        self.result= None
    
    def add(self, dim):
        """ Returns addition of two arrays of same dimension """
        self.arr_a= matrix(dim, dim) # Error spot
        self.arr_b= matrix(dim, dim)
        self.result= np.add(self.arr_a, self.arr_b)
        return self.result
    
    def sub(self, dim):
        """ Returns addition of two arrays of same dimension """
        self.arr_a= matrix(dim, dim) # Error spot
        self.arr_b= matrix(dim, dim)
        self.result= np.subtract(self.arr_a, self.arr_b)
        return self.result
    def multi(self, dim):
        """ Returns addition of two arrays of same dimension """
        self.arr_a= matrix(dim, dim) # Error spot
        self.arr_b= matrix(dim, dim)
        self.result= np.multiply(self.arr_a, self.arr_b)
        return self.result
    def  square(self, dim):
        """ Returns addition of two arrays of same dimension """
        self.arr_a= matrix(dim, dim) # Error spot
        # self.arr_b= matrix(dim, dim
        self.result= np.square(self.arr_a)
        return self.result

# Drive code.
if __name__ == '__main__':
    a= arithmetic()
    print(a.add(2))  
    print(a.sub(2))  
    print(a.multi(2))
    print(a.square(2))