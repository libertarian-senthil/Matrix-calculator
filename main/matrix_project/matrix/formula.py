# Status:active
"""
Creating a class performing matrix related formulae including square, transpose.
"""

import numpy as np

from mat_input import *

class formula:
    """ 
    Preforming matrix oriented operations- square of matrix, transpose of matrix.

    Attributes
    ----------
    arr_a : None
        Creating a matrix using numpy package.
    arr_b: None
        Creating a matrix using numpy package.    
    
    Methods
    -------
    square(dim=int)
        Return Square of a matrix.
    trans(dim:int)
        Return transpose of a matrix.
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
            Return Square of a matrix dimension

        """

        self.arr_a= matrix(dim, dim)
        try:
            self.result= np.square(self.arr_a)
        except:
            return ""
        else:
            return self.result
    
    def trans(self, dim): 
        """
         Return transpose of a matrix

         Parameters
         ----------
         dim : int
            The dimension of  matrix, for use by the addend or augend.

        Returns
        -------
            Return transpose of a matrix
        """

        self.arr_a= matrix(dim, dim) 
        try:
            self.result= np.transpose(self.arr_a)
        except: 
            return ""
        else:
            return self.result

# Drive code
# Currently this drive code is invalid needs to be changed
if __name__ == '__main__':
    a= formula()
    print(a.square(2))
    print(a.transpose(2))