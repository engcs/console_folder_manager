# https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
# https://andressa.dev/2019-07-20-using-pach-to-test-inputs/

import unittest
from io import StringIO
from unittest.mock import patch
from utils  import *

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

    def run_func_return_print(self, given_answer, expected_out, func, *args):
        with patch("builtins.input", return_value=given_answer), patch("sys.stdout", new=StringIO()) as fake_out:
            func(args)
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def run_func_return_value(self, given_answer, expected_out, func, *args):
        with patch("builtins.input", return_value=given_answer) as fake_out:
            func(args)
            self.assertEqual(fake_out.return_value, expected_out)

    def test_no(self):
        self.run_test("não", "você entrou com não")

    def test_yes(self):
        self.run_test("sim", "você entrou com sim")

    def test_meu_teste(self):
        self.run_func_return_print('valor', 'valor', meu_teste)

    def test_input_str(self):
        self.run_func_return_value('valor', 'valor', input_str)

if __name__ == "__main__":
    unittest.main()