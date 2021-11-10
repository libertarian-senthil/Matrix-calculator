# Status: active
"""
Creating class arithmetic in order to  perform arithmetic operations 
for matrices. the following operations are performed addtion, 
subtration, and multiplication.

classes
-------
arithmetic:
    A class performing arithmetic operations on matrices.
"""
import os, sys

file_path= "matrix_project\\matrix\\"
sys.path.append(os.path.dirname(file_path))

import numpy as np

from mat_input import *



class arithmetic:
    """Return the arithmetic operations for matrices. 
    
    Attributes
    ----------
    arr_a : None
        Creating a matrix using numpy package.
    arr_b: None
        Creating a matrix using numpy package.

    Methods
    -------
    add(dim=int)
        Returns addition of two arrays of same dimension.
    sub(dim=int)
        Returns subtraction of two arrays of same dimension.
    multi(dim)
        Returns multiplication of two arrays of same dimension.
    """
    
    def __init__(self, arr_a= None, arr_b= None):
        """
        parameters
        ----------
        arr_a: None
            Creating a matrix using numpy package.
        arr_b: None
            Creating a matrix using numpy package.
        """

        self.arr_a= np.array(arr_a)
        self.arr_b= np.array(arr_b)
        self.result= None
    
    def add(self, dim):
        """
        Perform addition on matrices.

        parameters
        ----------
        dim : int
            The dimension of  matrix, for use by the addend or augend.
        
        Returns
        -------
            An added value of two matrices.
        """

        self.arr_a= matrix(dim, dim) 
        self.arr_b= matrix(dim, dim)
        self.result= np.add(self.arr_a, self.arr_b)
        return self.result
    
    def sub(self, dim):
        """ 
        Perform subraction on matrices and return the result of the 
        subtraction of matrices.

        parameters
        ----------
        dim : int
            The dimension of  matrix, for use by both matrix to be 
            subtracted from another matrix.
        Returns
        -------
            An subtracted value of two matrices.
        """

        self.arr_a= matrix(dim, dim) 
        self.arr_b= matrix(dim, dim)
        self.result= np.subtract(self.arr_a, self.arr_b)
        return self.result
    
    def multi(self, dim):
        """ 
        Perform Multiplication on matrices and return the result of the 
        multiplication of matrices.

        parameters
        ----------
        dim : int
            The dimension of  matrix, for use by both matrix to be 
            multiplied.
        Returns
        -------
            An multiplied value of two matrices.
        """

        self.arr_a= matrix(dim, dim) 
        self.arr_b= matrix(dim, dim)
        self.result= np.multiply(self.arr_a, self.arr_b)
        return self.result        

# Drive code.
if __name__ == '__main__':
    a= arithmetic()
    print(a.add(eval(input("Enter the No. of dimensions:"))))  
    print(a.sub(eval(input("Enter the No.of dimensions:"))))  
    print(a.multi(eval(input("Enter the No. of dimensions:"))))
