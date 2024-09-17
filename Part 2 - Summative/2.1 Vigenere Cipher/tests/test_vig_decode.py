from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class TestVigEncode(TestCase):
    def test_vig_decode_with_spaces(self):
        self.assertEqual(vig_decode("LLWSIY VC", "TEST"), "THE QUICK")
    def test_vig_decode_with_lower(self):
        self.assertEqual(vig_decode("llWSIY VC", "TEST"), "THE QUICK")

    def test_vig_decode_with_numbers(self):
        self.assertEqual(vig_decode("3", "TEST"), "3")

    def test_vig_decode_with_text_and_numbers(self):
        self.assertEqual(vig_decode("LL3", "TEST"), "TH3")

    def test_vig_decode_with_swapped(self):
        self.assertEqual(vig_decode("LLWS", "THE QUICK!"), "TEST")

    def test_vig_decode_with_punc(self):
        self.assertEqual(vig_decode("LLWSIY VC!", "TEST"), "THE QUICK!")

    def test_vig_decode_with_everything(self):
        self.assertEqual(vig_decode("LLWsiy VC!34" , "TEST"), "THE QUICK!34")