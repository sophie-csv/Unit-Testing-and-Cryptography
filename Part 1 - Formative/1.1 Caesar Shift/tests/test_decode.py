from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode

class TestCaesarDecode(TestCase):
    def test_caesar_decode_with_spaces(self):
        self.assertEqual(caesar_decode("KHO OR", 3), "HEL LO")

    def test_caesar_decode_with_lower(self):
        self.assertEqual(caesar_decode("khoor", 3), "HELLO")

    def test_caesar_decode_with_numbers(self):
        self.assertEqual(caesar_decode("3", 3), "3")

    def test_caesar_decode_with_none(self):
        self.assertEqual(caesar_decode("",""), "")

    def test_caesar_decode_with_switched(self):
        self.assertEqual(caesar_decode("3", "hello"), "3")

    def test_caesar_decode_with_negative_numbers(self):
        self.assertEqual(caesar_decode("GDKKN", -1), "HELLO")

    def test_caesar_decode_with_punctuation(self):
        self.assertEqual(caesar_decode("KHOOR$", 3), "HELLO!")
