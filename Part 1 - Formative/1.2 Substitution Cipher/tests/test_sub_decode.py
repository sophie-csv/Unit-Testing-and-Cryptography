from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode

class TestCaesarDecode(TestCase):
    cipher_alphabet = 'WJKUXVBMIYDTPLHZGONCRSAEFQ'
    cipher_alphabet_with_punc = 'WJKUXVBMIYDTPLHZGONCRSAEFQ?"><:|}{+_)(*&^%$#@!'
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}|:"<>?'
    def test_sub_decode_with_spaces(self):
        self.assertEqual(sub_decode("CX EC", self.cipher_alphabet), "TE XT")
    def test_sub_decode_with_lower(self):
        self.assertEqual(sub_decode("CXEC", self.cipher_alphabet), "TEXT")
    def test_sub_decode_with_numbers(self):
        self.assertEqual(sub_decode("M3", self.cipher_alphabet), "H")

    def test_sub_decode_with_none(self):
        self.assertEqual(sub_decode("", self.cipher_alphabet), "")

    def test_sub_decode_with_switched(self):
        self.assertEqual(sub_decode(self.cipher_alphabet, "HELLO"), "WJKUXVBMIYDTPLHZGONCRSAEFQ")

    def test_sub_decode_with_punctuation(self):
        self.assertEqual(sub_decode("MXTTH?", self.cipher_alphabet_with_punc), "HELLO!")

    def test_sub_decode_with_everything(self):
        self.assertEqual(sub_decode("Texx3!(& thankS", self.cipher_alphabet_with_punc), "LXEE?+} LOWSCV")

    def test_sub_decode_with_alph(self):
        self.assertEqual(sub_decode(self.cipher_alphabet_with_punc, self.cipher_alphabet_with_punc), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}|:"<>?')