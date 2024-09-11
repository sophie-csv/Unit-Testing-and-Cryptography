from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode

class TestCaesarDecode(TestCase):
    cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
    cipher_alphabet_with_punc = 'WJKUXVBMIYDTPLHZGONCRSAEFQ?"><:|}{+_)(*&^%$#@!)}'
    def test_sub_encode_with_spaces(self):
        self.assertEqual(sub_encode("TE XT", self.cipher_alphabet), "CX EC")
    def test_sub_encode_with_lower(self):
        self.assertEqual(sub_encode("text", self.cipher_alphabet), "CXEC")
    def test_sub_encode_with_numbers(self):
        self.assertEqual(sub_encode("3h", self.cipher_alphabet), "M")

    def test_sub_encode_with_none(self):
        self.assertEqual(sub_encode("", self.cipher_alphabet), "")

    def test_sub_encode_with_switched(self):
        self.assertEqual(sub_encode(self.cipher_alphabet, "HELLO"), "WJKUXVBMIYDTPLHZGONCRSAEFQ")

    def test_sub_encode_with_punctuation(self):
        self.assertEqual(sub_encode("HELLO!", self.cipher_alphabet_with_punc), "MXTTH?")

    def test_sub_encode_with_everything(self):
        self.assertEqual(sub_encode("Texx3!(& thankS", self.cipher_alphabet_with_punc), "CXEE?+} CMWLDN")