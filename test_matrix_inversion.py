
import unittest

from matrix_inversion import invert_2x2


class TestMatrixInversion(unittest.TestCase):

    # Test the 2x2 inversion using the example in the handout.
    def test_invert_2x2(self):
        a, b, c, d = 4, 3, 1, 1
        inverted_matrix = invert_2x2(a, b, c, d)
        e, f, g, h = inverted_matrix
        self.assertEqual(e, 1)
        self.assertEqual(f, -3)
        self.assertEqual(g, -1)
        self.assertEqual(h, 4)
