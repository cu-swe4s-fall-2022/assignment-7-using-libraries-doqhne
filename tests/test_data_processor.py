import unittest
import data_processor as dp
import random
import numpy as np
import pandas as pd
import os
import sys
import pathlib as pl
sys.path.append('../')


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.iris = 'iris.data'


    def tearDown(self):
        return None
 

    def test_get_random_matrix(self):
        # Make sure matrix is correct shape
        self.assertEqual(dp.get_random_matrix(4, 2).shape, (4, 2))
        
        # Negative test
        self.assertNotEqual(dp.get_random_matrix(4, 2).shape, (2, 4))
        
        # Make sure inputs are integers
        with self.assertRaises(TypeError):
            dp.get_random_matrix(3.5, 13)

        # Make sure inputs are greater than 0
        with self.assertRaises(ValueError):
            dp.get_random_matrix(-3, 0)


    def test_get_file_dimensions(self):
        # Positive test
        self.assertEqual(dp.get_file_dimensions(self.iris), (149, 5))
        
        # Negative test
        self.assertNotEqual(dp.get_file_dimensions(self.iris), (5, 149))
    
    
    def test_write_matrix_to_file(self):
        # Positive test
        self.assertEqual(dp.write_matrix_to_file(3, 2, 'test_file.csv'), None)
        
        # CHeck file is outputted
        path = pl.Path("./test_file.csv")
        self.assertTrue(path.is_file())
        self.assertTrue(path.parent.is_dir())

        
        