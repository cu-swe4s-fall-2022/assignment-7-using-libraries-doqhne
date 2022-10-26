import unittest
import data_processor as dp
import random
import numpy as np
import pandas as pd
import os
import sys
sys.path.append('../')


class TestUtils(unittest.TestCase):
    def test_get_random_matrix(self):
        # Make sure matrix is correct shape
        self.assertEqual(dp.get_random_matrix(4, 2).shape, (4, 2))