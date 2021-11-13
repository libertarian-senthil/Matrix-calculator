# Status:active
"""
Creating a class performing matrix related formulae including square, transpose.
"""

import numpy as np

from mat_input import *

class formula:
    """ 
    Preforming matrix oriented operations- square of matrix, transpose oof matrix.

    Attributes
    ----------
    arr_a : None
        Creating a matrix using numpy package.
    arr_b: None
        Creating a matrix using numpy package.    
    
    Methods
    -------
    square(dim=int)
        Return Square of two arrays of same dimension


    """
    
    def __init__(self, arr_a = None, arr_b = None):    
        """
        Parameters
        ----------
        arr_a : None
            Creating a matrix using numpy package.
        arr_b: None
            Creating a matrix using numpy package.                    
        """

        self.arr_a= np.array(arr_a)
        self.result= None
        
    def  square(self, dim):
        """
        Perform squaring of a given matrix.

        Parameters
        ----------
        dim : int
            The dimension of  matrix, for use by the addend or augend.
        
        Returns
        -------
            Return Square of two arrays of same dimension

        """

        self.arr_a= matrix(dim, dim)
        try:
            self.result= np.square(self.arr_a)
        except:
            return ""
        else:
            return self.result
    
    def trans(self, dim): 
        """ Returns Transpose of two arrays of same dimension """
        self.arr_a= matrix(dim, dim) 
        try:
            self.result= np.transpose(self.arr_a)
        except: 
            return ""
        else:
            return self.result

if __name__ == '__main__':
    a= formula()
    print(a.square(2))
    print(a.transpose(2))

#yet to be completed
