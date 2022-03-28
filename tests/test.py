import unittest

import python_test_package

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(python_test_package.extremely_useful_function(), 42)
