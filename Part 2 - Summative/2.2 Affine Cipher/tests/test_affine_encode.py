from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode

class TestVigEncode(TestCase):
    def test_vig_encode_with_spaces(self):
        self.assertEqual(affine_encode("THE QUICK", "TEST"), "LLWSIY VC")
    def test_vig_encode_with_lower(self):
        self.assertEqual(affine_encode("THE quick", "TEST"), "LLWSIY VC")

    def test_vig_encode_with_numbers(self):
        self.assertEqual(affine_encode("3", "TEST"), "3")

    def test_vig_encode_with_text_and_numbers(self):
        self.assertEqual(affine_encode("TH3", "TEST"), "LL3")

    def test_vig_encode_with_swapped(self):
        self.assertEqual(affine_encode("TEST", "THE QUICK!"), "LLWS")

    def test_vig_encode_with_punc(self):
        self.assertEqual(affine_encode("THE QUICK!", "TEST"), "LLWSIY VC!")

    def test_vig_encode_with_everything(self):
        self.assertEqual(affine_encode("THE quick!34", "TEST"), "LLWSIY VC!34")