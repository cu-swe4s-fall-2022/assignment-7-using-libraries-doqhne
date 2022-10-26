'''
Functions to aid in data processing

    * get_random_matrix : Creates an MxN matrix filled with random numbers
    * get_file_dimensions : Find the shape of a csv file
    * write_matrix_to_file : Write a random matrix to a csv file
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
    '''
    Find the shape of a csv file

    Parameters
    ----------
    file_name : The name of the csv file

    Returns
    -------
    dims : The dimensions of the file (rows, cols)

    '''
    try:
        file = pd.read_csv(file_name)
    except FileNotFoundError:
        print("Could not find ", file_name)
    except PermissionError:
        print("Could not find ", file_name)

    dims = file.shape

    return dims


def write_matrix_to_file(num_rows, num_columns, file_name):
    '''
    Writes an MxN matrix filled with random numbers to a csv file

    Parameters
    ----------
    num_rows : The number of rows in the matrix. Expects int>0
    num_cols : The number of columns in the matrix. Expects int>0
    file_name : The name of file to write to

    Returns
    -------
    None,  a csv file is created with name file_name

    '''
    # Create a random matrix
    matrix = get_random_matrix(num_rows, num_columns)
    
    # Create a header
    header=np.arange(0, num_columns)
    header_str = np.array2string(header, separator=',')
    header_str = header_str.replace('[', '')
    header_str = header_str.replace(']', '')
    
    # Save the file as a csv file
    np.savetxt(file_name, matrix, delimiter=',', header=header_str)

    return None
