# https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests

import unittest
from io import StringIO
from unittest.mock import patch


def answer():
    ans = input("Entre 'sim' ou 'não': ")
    if ans == "sim":
        print("você entrou com sim")
    if ans == "não":
        print("você entrou com não")


class MyTestCase(unittest.TestCase):
    def run_test(self, given_answer, expected_out):
        with patch("builtins.input", return_value=given_answer), patch("sys.stdout", new=StringIO()) as fake_out:
            answer()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def test_no(self):
        self.run_test("não", "você entrou com não")

    def test_yes(self):
        self.run_test("sim", "você entrou com sim")

if __name__ == "__main__":
    unittest.main()