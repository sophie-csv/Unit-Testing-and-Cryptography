from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode

class TestAffineEncode(TestCase):
    def test_affine_encode_with_spaces(self):
        self.assertEqual(affine_encode("HELLOWORLD", 3, 9), "EVQQZXZIQS")
    def test_affine_encode_with_lower(self):
        self.assertEqual(affine_encode("HELLOWORLD",3,9), "EVQQZXZIQS")

    def test_affine_encode_with_numbers(self):
        self.assertEqual(affine_encode("3", 3, 9), "")

    def test_affine_encode_with_text_and_numbers(self):
        self.assertEqual(affine_encode("HELLOWORLD", 3, 9), "EVQQZXZIQS")

    def test_affine_encode_with_punc(self):
        self.assertEqual(affine_encode("HELLOWORLD!", 3,9), "EVQQZXZIQS")
