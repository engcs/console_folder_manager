# https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
# https://andressa.dev/2019-07-20-using-pach-to-test-inputs/
import os.path
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


class TestCreateAndDeleteDirs(unittest.TestCase):

    temp_folder_name = "TEST_FOLDER"
    temp_file_name = "testfile.txt"
    temp_file_path = os.path.join(temp_folder_name, "testfile.txt")

    def setUp(self):
        if os.path.isdir(self.temp_folder_name):
            shutil.rmtree(self.temp_folder_name)

    def test_create_and_delete_empty_folder(self):
        self.assertFalse(os.path.isdir(self.temp_folder_name), "Inital fail, folder already exists.")
        make_dir(self.temp_folder_name)
        self.assertTrue(os.path.isdir(self.temp_folder_name), "Failed to create the folder.")
        rm_dir(self.temp_folder_name)
        self.assertFalse(os.path.isdir(self.temp_folder_name), "Failed to remove the empty folder.")

    def test_create_and_delete_filed_folder(self):
        self.assertFalse(os.path.isdir(self.temp_folder_name), "Inital fail, folder already exists.")
        make_dir(self.temp_folder_name)
        self.assertTrue(os.path.isdir(self.temp_folder_name), "Failed to create the folder.")
        with open(self.temp_file_path, "w") as f:
            f.write("Delete me!")
        self.assertTrue(os.path.isfile(self.temp_file_path), "Failed to create the file.")
        rm_dir(self.temp_folder_name)
        self.assertFalse(os.path.isdir(self.temp_folder_name), "Failed to remove the filed folder.")


if __name__ == "__main__":
    unittest.main()
