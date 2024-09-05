from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestCaesarEncode(TestCase):
    def test_caesar_encode_with_spaces(self):
        self.assertEqual(insert_string("HEL LO", 3), "MJQQT")

    def test_insert_string_two_words_with_uppercase(self):
        self.assertEqual(insert_string("apple", "ORANGE"), "apORANGEple")

    def test_insert_string_empty_insert(self):
        self.assertEqual(insert_string("apple", ""), "apple")
