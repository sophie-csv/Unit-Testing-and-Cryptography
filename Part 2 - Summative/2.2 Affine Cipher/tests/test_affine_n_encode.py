from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_encode

class TestAffineNDecode(TestCase):
    def test_affine_n_encode(self):
        self.assertEqual(affine_n_encode("COOL", 3, 3, 121), "XURYWT")

    def test_affine_n_encode_other(self):
        self.assertEqual(affine_n_encode("COOL", 2, 3, 121), "XUHN")



