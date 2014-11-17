#!/usr/bin/env python
""" Tests for YATSM scripts
"""
import os
import shutil
import subprocess
import sys
import unittest

import numpy as np
from osgeo import gdal


def _run(script, args):
    """ Use subprocess to run script with arguments

    Args:
      script (str): script filename to run
      args (list): program arguments

    Returns:
      tuple: stdout and exit code

    """
    proc = subprocess.Popen([script] + args,
                            stdout=subprocess.PIPE
                            )

    stdout = proc.communicate()[0]
    retcode = proc.returncode

    return stdout, retcode


class Test_YATSMMap(unittest.TestCase):

    def setUp(self):
        """ Setup test data filenames and load known truth dataset """
        # Test data
        self.root = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'data')
        self.result_dir = os.path.join(self.root, 'YATSM')
        self.robust_result_dir = os.path.join(self.root, 'YATSM_ROBUST')
        self.data_cache = os.path.join(self.root, 'cache')
        self.example_img = os.path.join(self.root, 'example_img')

        # Answers
        self.outdir = os.path.join(self.root, 'outdir')

        if not os.path.isdir(self.outdir):
            os.makedirs(self.outdir)

    def tearDown(self):
        """ Deletes answer directory """
        if os.path.isdir(self.outdir):
            shutil.rmtree(self.outdir)

# Test coefficients
    def test_coef_result(self):
        """ Test creating coefficient map """
        args = '--root {r} coef 2000-06-01 {o}'.format(
            r=self.root,
            o=os.path.join(self.outdir, 'coef_all.gtif')).split(' ')

        msg, retcode = _run(args)
        self.assertEqual(retcode, 0)

    def test_coef_result_robust(self):
        """ Test creating robust coefficient map """

        # Test robust coefficients
        args = '--root {r} --result {rr} --robust coef 2000-06-01 {o}'.format(
            r=self.root,
            rr=self.robust_result_dir,
            o=os.path.join(self.outdir, 'coef_all.gtif')).split(' ')

        msg, retcode = _run(args)
        self.assertEqual(retcode, 0)

        # Test robust coefficients, expecting error
        args = '--root {r} --robust coef 2000-06-01 {o}'.format(
            r=self.root,
            o=os.path.join(self.outdir, 'coef_all.gtif')).split(' ')
        msg, retcode = _run(args)

        self.assertEqual(retcode, 1)

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
