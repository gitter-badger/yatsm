#!/usr/bin/env python
""" Tests for YATSM scripts
"""
import os
import subprocess
import sys
import unittest

import numpy as np
from osgeo import gdal


class Test_YATSMMap(unittest.TestCase):


    def set_up(self):
        """ Setup test data filenames and load known truth dataset """
        # Test data
        self.root = 'data'
        self.result_dir = os.path.join(self.root, 'YATSM')
        self.data_cache = os.path.join(self.root, 'cache')
        self.example_img = os.path.join(self.root, 'example_img')

        # Answers

# Test coefficients
    def test_coef_result(self):
        """ Test correctness of result """
        # Test against truth for regular coefficients
        # Test against truth for robust coefficients
        pass

    def test_coef_bands(self):
        """ Test if correct bands are output """
        # Test bands outputs
        # Test coefficient outputs
        pass

    def test_coef_before_after(self):
        """ Test use of --before and --after flags """
        pass

# Test prediction
# Test classification
# Test optional arguments
    def test_ndv(self):
        """ Test output file NoDataValue """
        pass

    def test_output_format(self):
        """ Test output GDAL file format """
        pass

    def test_date_format(self):
        """ Test input date format type """
        pass


if __name__ == '__main__':
    unittest.main()
