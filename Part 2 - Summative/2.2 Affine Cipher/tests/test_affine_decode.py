from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode

class TestAffineDecode(TestCase):
    def test_affine_decode_with_spaces(self):
        self.assertEqual(affine_decode("EVQQZ XZIQS", 3, 9), "HELLOWORLD")
    def test_affine_decode_with_lower(self):
        self.assertEqual(affine_decode("EVQQZXZIQS",3,9), "HELLOWORLD")

    def test_affine_decode_with_nothing(self):
        self.assertEqual(affine_decode("", 3, 9), "")

    def test_affine_decode_with_numbers(self):
        self.assertEqual(affine_decode("3", 3, 9), "")

    def test_affine_decode_with_text_and_numbers(self):
        self.assertEqual(affine_decode("EVQQZXZIQS2", 3, 9), "HELLOWORLD")

    def test_affine_decode_with_punc(self):
        self.assertEqual(affine_decode("EVQQZXZIQS!", 3,9), "HELLOWORLD")