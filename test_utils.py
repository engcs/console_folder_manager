# https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
# https://andressa.dev/2019-07-20-using-pach-to-test-inputs/

import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from utils import *


class TestInputStr(unittest.TestCase):

    # required=True
    @patch(target="builtins.input", new=MagicMock(return_value='123'))
    def test_input_str_123_required_True(self):
        self.assertEqual(first=input_str(required=True), second='123')

    @patch(target="builtins.input", new=MagicMock(return_value='abc'))
    def test_input_str_abc_required_True(self):
        self.assertEqual(first=input_str(required=True), second='abc')

    def test_input_str_blank_required_True(self):
        # Entra primeiro com vazio e depois com um dado válido para sair do loop
        with patch("builtins.input", side_effect=["", "teste"]), patch("sys.stdout", new=StringIO()) as fake_out:
            input_str(required=True)
            self.assertEqual(fake_out.getvalue().strip(),
                             Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)

    # required=False
    @patch(target="builtins.input", new=MagicMock(return_value='123'))
    def test_input_str_123_required_False(self):
        self.assertEqual(first=input_str(required=False), second='123')

    @patch(target="builtins.input", new=MagicMock(return_value='abc'))
    def test_input_str_abc_required_False(self):
        self.assertEqual(first=input_str(required=False), second='abc')

    @patch(target="builtins.input", new=MagicMock(return_value=''))
    def test_input_str_blank_required_False(self):
        self.assertEqual(first=input_str(required=False), second=None)


class TestInputStrWithExit(unittest.TestCase):

    # required=True
    @patch(target="builtins.input", new=MagicMock(return_value='123'))
    def test_input_str_123_required_True(self):
        self.assertEqual(first=input_str_with_exit(required=True), second='123')

    @patch(target="builtins.input", new=MagicMock(return_value='abc'))
    def test_input_str_abc_required_True(self):
        self.assertEqual(first=input_str_with_exit(required=True), second='abc')

    @patch(target="builtins.input", new=MagicMock(return_value='exit'))
    def test_input_str_exit_required_True(self):
        self.assertEqual(first=input_str_with_exit(required=True), second='exit')

    def test_input_str_blank_required_True(self):
        # Entra primeiro com vazio e depois com um dado válido para sair do loop
        with patch("builtins.input", side_effect=['', 'teste']), patch("sys.stdout", new=StringIO()) as fake_out:
            input_str_with_exit(required=True)
            self.assertEqual(fake_out.getvalue().strip(),
                             Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)

    # required=False
    @patch(target="builtins.input", new=MagicMock(return_value='123'))
    def test_input_str_123_required_False(self):
        self.assertEqual(first=input_str_with_exit(required=False), second='123')

    @patch(target="builtins.input", new=MagicMock(return_value='abc'))
    def test_input_str_abc_required_False(self):
        self.assertEqual(first=input_str_with_exit(required=False), second='abc')

    @patch(target="builtins.input", new=MagicMock(return_value=''))
    def test_input_str_blank_required_False(self):
        self.assertEqual(first=input_str_with_exit(required=False), second=None)


class TestInputInt(unittest.TestCase):

    # required=True
    @patch(target="builtins.input", new=MagicMock(return_value='123'))
    def test_input_int_123_required_True(self):
        self.assertEqual(first=input_int(required=True), second=123)

    def test_input_int_abc_required_True(self):
        # Entra primeiro com vazio e depois com um dado válido para sair do loop
        with patch("builtins.input", side_effect=['abc', '123']), patch("sys.stdout", new=StringIO()) as fake_out:
            input_int(required=True)
            self.assertEqual(fake_out.getvalue().strip(),
                             Fore.RED + "Error! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)

    def test_input_int_blank_required_True(self):
        # Entra primeiro com vazio e depois com um dado válido para sair do loop
        with patch("builtins.input", side_effect=['', '123']), patch("sys.stdout", new=StringIO()) as fake_out:
            input_int(required=True)
            self.assertEqual(fake_out.getvalue().strip(),
                             Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)

    # required=False
    @patch(target="builtins.input", new=MagicMock(return_value='123'))
    def test_input_int_123_required_False(self):
        self.assertEqual(first=input_int(required=False), second=123)

    def test_input_int_abc_required_False(self):
        # Entra primeiro com vazio e depois com um dado válido para sair do loop
        with patch("builtins.input", side_effect=['abc', '123']), patch("sys.stdout", new=StringIO()) as fake_out:
            input_int(required=False)
            self.assertEqual(fake_out.getvalue().strip(),
                             Fore.RED + "Error! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)

    @patch(target="builtins.input", new=MagicMock(return_value=''))
    def test_input_int_blank_required_False(self):
        self.assertEqual(first=input_int(required=False), second=None)


class TestInputIntWithExit(unittest.TestCase):

    # required=True
    @patch(target="builtins.input", new=MagicMock(return_value='123'))
    def test_input_int_123_required_True(self):
        self.assertEqual(first=input_int_with_exit(required=True), second=123)

    def test_input_int_abc_required_True(self):
        # Entra primeiro com vazio e depois com um dado válido para sair do loop
        with patch("builtins.input", side_effect=['abc', '123']), patch("sys.stdout", new=StringIO()) as fake_out:
            input_int_with_exit(required=True)
            self.assertEqual(fake_out.getvalue().strip(),
                             Fore.RED + "Error! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)

    def test_input_int_blank_required_True(self):
        # Entra primeiro com vazio e depois com um dado válido para sair do loop
        with patch("builtins.input", side_effect=['', '123']), patch("sys.stdout", new=StringIO()) as fake_out:
            input_int_with_exit(required=True)
            self.assertEqual(fake_out.getvalue().strip(),
                             Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)

    @patch(target="builtins.input", new=MagicMock(return_value='exit'))
    def test_input_int_exit_required_True(self):
        self.assertEqual(first=input_int_with_exit(required=True), second='exit')

    # required=False
    @patch(target="builtins.input", new=MagicMock(return_value='123'))
    def test_input_int_123_required_False(self):
        self.assertEqual(first=input_int_with_exit(required=False), second=123)

    def test_input_int_abc_required_False(self):
        # Entra primeiro com vazio e depois com um dado válido para sair do loop
        with patch("builtins.input", side_effect=['abc', '123']), patch("sys.stdout", new=StringIO()) as fake_out:
            input_int_with_exit(required=False)
            self.assertEqual(fake_out.getvalue().strip(),
                             Fore.RED + "Error! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)

    @patch(target="builtins.input", new=MagicMock(return_value=''))
    def test_input_int_blank_required_False(self):
        self.assertEqual(first=input_int_with_exit(required=False), second=None)


if __name__ == "__main__":
    unittest.main()
