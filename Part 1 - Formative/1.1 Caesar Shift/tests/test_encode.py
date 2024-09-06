from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestCaesarEncode(TestCase):
    def test_caesar_encode_with_spaces(self):
        self.assertEqual(caesar_encode("HEL LO", 3), "KHO OR")

    def test_caesar_encode_with_lower(self):
        self.assertEqual(caesar_encode("hello", 3), "KHOOR")

    def test_caesar_encode_with_numbers(self):
        self.assertEqual(caesar_encode("3", 3), "3")

    def test_caesar_encode_with_none(self):
        self.assertEqual(caesar_encode("",""), "")

    def test_caesar_encode_with_switched(self):
        self.assertEqual(caesar_encode("3", "hello"), "3")

    def test_caesar_encode_with_negative_numbers(self):
        self.assertEqual(caesar_encode("HELLO", -1), "GDKKN")

    def test_caesar_encode_with_punctuation(self):
        self.assertEqual(caesar_encode("HELLO!", 3), "KHOOR$")