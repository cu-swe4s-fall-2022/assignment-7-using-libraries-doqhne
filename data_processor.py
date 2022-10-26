'''
Functions to aid in data processing

    * get_random_matrix : Creates an MxN matrix filled with random numbers
    * get_file_dimensions :
    * write_matrix_to_file : 
'''

import numpy as np
import pandas as pd


def get_random_matrix(num_rows, num_columns):
    '''
    Creates an MxN matrix filled with random numbers

    Parameters
    ----------
    num_rows : The number of rows in the matrix. Expects int>0
    num_cols : The number of columns in the matrix. Expects int>0

    Returns
    -------
    matrix : An matrix with random numbers

    '''
    # Make sure inputs are integers
    if not isinstance(num_rows, int):
        raise TypeError("num_rows must be type int")
    if not isinstance(num_columns, int):
        raise TypeError("num_columns must be type int")
    
    # Make sure inputs are greater than 0
    if (num_rows<0 or num_columns<0):
        raise ValueError("Inputs must be integers greater than 0")

    matrix = np.random.rand(num_rows, num_columns)

    return matrix


def get_file_dimensions(file_name):
    file = pd.read_csv(file_name)
    return file.shape

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
