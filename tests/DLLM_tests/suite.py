# -*-mode: python; py-indent-offset: 4; tab-width: 8; coding: iso-8859-1 -*-
# Copyright: EADS

import unittest

from test_wing_param import TestWingParam
from test_DLLM_simple import TestDLLMSimple

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestWingParam))
    suite.addTest(unittest.makeSuite(TestDLLMSimple))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=10).run(suite())