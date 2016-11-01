
import unittest

from data_compiler import compile_data


class TestDataCompiler(unittest.TestCase):

    def test_data_compiler(self):
        voltages = [1.0, 2.0, 3.0, 3.0, 3.0, 4.0]
        currents = [18.0, 19.0, 20.0, 21.0, 22.0, 23.0]
        compiled_data = compile_data(voltages, currents)
        s1, ss1, c1 = compiled_data[1.0]
        s2, ss2, c2 = compiled_data[2.0]
        s3, ss3, c3 = compiled_data[3.0]
        s4, ss4, c4 = compiled_data[4.0]
        self.assertEqual(s1, 18.0)
        self.assertEqual(ss1, 324.0)
        self.assertEqual(c1, 1)
        self.assertEqual(s2, 19.0)
        self.assertEqual(ss2, 361.0)
        self.assertEqual(c2, 1)
        self.assertEqual(s3, 63.0)
        self.assertEqual(ss3, 1325.0)
        self.assertEqual(c3, 3)
        self.assertEqual(s4, 23.0)
        self.assertEqual(ss4, 529.0)
        self.assertEqual(c4, 1)
