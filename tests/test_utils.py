# https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
# https://andressa.dev/2019-07-20-using-pach-to-test-inputs/
import os.path
import unittest
from io import StringIO
from unittest.mock import MagicMock, Mock, patch

from app.utils import *


# class TestInputStr(unittest.TestCase):
#
#     """ Test if input_str works with required=True """
#
#     @patch(target="builtins.input", new=MagicMock(return_value='123'))
#     def test_input_str_123_required_True(self):
#         self.assertEqual(first=input_str(required=True), second='123')
#
#     @patch(target="builtins.input", new=MagicMock(return_value='abc'))
#     def test_input_str_abc_required_True(self):
#         self.assertEqual(first=input_str(required=True), second='abc')
#
#     def test_input_str_blank_required_True(self):
#         # Entra primeiro com vazio e depois com um dado válido para sair do loop
#         with patch("builtins.input", side_effect=["", "teste"]), patch("sys.stdout", new=StringIO()) as fake_out:
#             input_str(required=True)
#             self.assertEqual(fake_out.getvalue().strip(),
#                              Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
#
#     """ Test if input_str works with required=False """
#
#     @patch(target="builtins.input", new=MagicMock(return_value='123'))
#     def test_input_str_123_required_False(self):
#         self.assertEqual(first=input_str(required=False), second='123')
#
#     @patch(target="builtins.input", new=MagicMock(return_value='abc'))
#     def test_input_str_abc_required_False(self):
#         self.assertEqual(first=input_str(required=False), second='abc')
#
#     @patch(target="builtins.input", new=MagicMock(return_value=''))
#     def test_input_str_blank_required_False(self):
#         self.assertEqual(first=input_str(required=False), second=None)
#
#     """ Test if input_str works with required=True and escape=['exit'] """
#
#     @patch(target="builtins.input", new=MagicMock(return_value='123'))
#     def test_input_str_123_required_True_escape_exit(self):
#         self.assertEqual(first=input_str(required=True, escape=['exit']), second='123')
#
#     @patch(target="builtins.input", new=MagicMock(return_value='abc'))
#     def test_input_str_abc_required_True_escape_exit(self):
#         self.assertEqual(first=input_str(required=True, escape=['exit']), second='abc')
#
#     @patch(target="builtins.input", new=MagicMock(return_value='exit'))
#     def test_input_str_exit_required_True_escape_exit(self):
#         self.assertEqual(first=input_str(required=True, escape=['exit']), second='exit')
#
#     def test_input_str_blank_required_True_escape_exit(self):
#         # Entra primeiro com vazio e depois com um dado válido para sair do loop
#         with patch("builtins.input", side_effect=['', 'teste']), patch("sys.stdout", new=StringIO()) as fake_out:
#             input_str(required=True, escape=['exit'])
#             self.assertEqual(fake_out.getvalue().strip(),
#                              Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
#
#     """ Test if input_str works with required=False and escape=['exit'] """
#
#     @patch(target="builtins.input", new=MagicMock(return_value='123'))
#     def test_input_str_123_required_False_escape_exit(self):
#         self.assertEqual(first=input_str(required=False, escape=['exit']), second='123')
#
#     @patch(target="builtins.input", new=MagicMock(return_value='abc'))
#     def test_input_str_abc_required_False_escape_exit(self):
#         self.assertEqual(first=input_str(required=False, escape=['exit']), second='abc')
#
#     @patch(target="builtins.input", new=MagicMock(return_value=''))
#     def test_input_str_blank_required_False_escape_exit(self):
#         self.assertEqual(first=input_str(required=False, escape=['exit']), second=None)


class TestInputInt(unittest.TestCase):

    """###############################
            @required = True
    ###############################"""

    @patch(target="builtins.input", new=Mock(return_value='123'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_positive_123_required_True(self, fake_out):
        esperado = 123
        recebido = input_int(required=True)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='-123'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_negative_123_required_True(self, fake_out):
        esperado = -123
        recebido = input_int(required=True)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(side_effect=['abc', '123']))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_abc_required_True(self, fake_out):
        input_int(required=True)
        esperado = error("O valor informado não é um número válido.")
        recebido = fake_out.getvalue().strip()
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(side_effect=[' ', '123']))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_blank_required_True(self, fake_out):
        input_int(required=True)
        esperado = error("O campo é obrigatório.")
        recebido = fake_out.getvalue().strip()
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='exit'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_required_True(self, fake_out):
        esperado = 'exit'
        recebido = input_int(required=True, escape=['exit', 'saída'])
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='sair'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_sair_required_True(self, fake_out):
        esperado = 'sair'
        recebido = input_int(required=True, escape=['exit', 'sair'])
        self.assertEqual(recebido, esperado)


    @patch(target="builtins.input", new=Mock(return_value='3'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_positive_123_required_True(self, fake_out):
        esperado = 3
        recebido = input_int(required=True, allowed=range(1, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='-3'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_negative_123_required_True(self, fake_out):
        esperado = -3
        recebido = input_int(required=True, allowed=range(-10, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='0'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_with_valid_integers_required_True(self, fake_out):
        esperado = 0
        recebido = input_int(required=True, allowed=range(-10, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(side_effect=['123', '3']))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_with_invalid_integers_required_True(self, fake_out):
        input_int(required=True, allowed=range(-10, 5))
        esperado = error("Insira um valor válido.")
        recebido = fake_out.getvalue().strip()
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value=''))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_without_integers_required_True(self, fake_out):
        with self.assertRaises(ValueError):
            input_int(required=True, allowed=['1', 'a', '@'])

    """###############################
            @required = False
    ###############################"""

    @patch(target="builtins.input", new=Mock(return_value='123'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_positive_123_required_False(self, fake_out):
        esperado = 123
        recebido = input_int(required=False)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='-123'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_negative_123_required_False(self, fake_out):
        esperado = -123
        recebido = input_int(required=False)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(side_effect=['abc', '123']))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_abc_required_False(self, fake_out):
        input_int(required=False)
        esperado = error("O valor informado não é um número válido.")
        recebido = fake_out.getvalue().strip()
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value=''))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_blank_required_False(self, fake_out):
        esperado = None
        recebido = input_int(required=False)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value=' '))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_space_required_False(self, fake_out):
        esperado = None
        recebido = input_int(required=False)
        self.assertEqual(recebido, esperado)


    @patch(target="builtins.input", new=Mock(return_value='exit'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_required_False(self, fake_out):
        esperado = 'exit'
        recebido = input_int(required=False, escape=['exit', 'sair'])
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='sair'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_sair_required_False(self, fake_out):
        esperado = 'sair'
        recebido = input_int(required=False, escape=['exit', 'sair'])
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='sair'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_sair_required_False(self, fake_out):
        esperado = 'sair'
        recebido = input_int(required=False, escape=['exit', 'sair'])
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='3'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_positive_123_required_False(self, fake_out):
        esperado = 3
        recebido = input_int(required=False, allowed=range(1, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='-3'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_negative_123_required_False(self, fake_out):
        esperado = -3
        recebido = input_int(required=False, allowed=range(-10, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='0'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_with_valid_integers_required_False(self, fake_out):
        esperado = 0
        recebido = input_int(required=False, allowed=range(-10, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(side_effect=['123', '3']))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_with_invalid_integers_required_False(self, fake_out):
        input_int(required=False, allowed=range(-10, 5))
        esperado = error("Insira um valor válido.")
        recebido = fake_out.getvalue().strip()
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value=''))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_without_integers_required_False(self, fake_out):
        with self.assertRaises(ValueError):
            input_int(required=False, allowed=['1', 'a', '@'])


class TestInputStr(unittest.TestCase):

    """###############################
            @required = True
    ###############################"""

    @patch(target="builtins.input", new=Mock(return_value='123'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_positive_123_required_True(self, fake_out):
        esperado = '123'
        recebido = input_str(required=True)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='-123'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_negative_123_required_True(self, fake_out):
        esperado = '-123'
        recebido = input_str(required=True)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='abc'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_abc_required_True(self, fake_out):
        esperado = 'abc'
        recebido = input_str(required=True)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(side_effect=[' ', 'abc']))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_blank_required_True(self, fake_out):
        input_str(required=True)
        esperado = error("O campo é obrigatório.")
        recebido = fake_out.getvalue().strip()
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='exit'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_required_True(self, fake_out):
        esperado = 'exit'
        recebido = input_str(required=True, escape=['exit', 'sair'])
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='sair'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_sair_required_True(self, fake_out):
        esperado = 'sair'
        recebido = input_str(required=True, escape=['exit', 'sair'])
        self.assertEqual(recebido, esperado)


    @patch(target="builtins.input", new=Mock(return_value='3'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_positive_123_required_True(self, fake_out):
        esperado = '3'
        recebido = input_str(required=True, allowed=range(1, 5))
        self.assertEqual(recebido, esperado)


    @patch(target="builtins.input", new=Mock(return_value='-3'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_negative_123_required_True(self, fake_out):
        esperado = '-3'
        recebido = input_str(required=True, allowed=range(-10, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='0'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_with_valid_integers_required_True(self, fake_out):
        esperado = '0'
        recebido = input_str(required=True, allowed=range(-10, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(side_effect=['123', '3']))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_with_invalid_integers_required_True(self, fake_out):
        input_str(required=True, allowed=range(-10, 5))
        esperado = error("Insira uma entrada válida.")
        recebido = fake_out.getvalue().strip()
        self.assertEqual(recebido, esperado)

    """###############################
            @required = False
    ###############################"""

    @patch(target="builtins.input", new=Mock(return_value='123'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_positive_123_required_False(self, fake_out):
        esperado = '123'
        recebido = input_str(required=False)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='-123'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_negative_123_required_False(self, fake_out):
        esperado = '-123'
        recebido = input_str(required=False)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='abc'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_abc_required_False(self, fake_out):
        esperado = 'abc'
        recebido = input_str(required=False)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value=''))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_blank_required_False(self, fake_out):
        esperado = None
        recebido = input_str(required=False)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value=' '))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_space_required_False(self, fake_out):
        esperado = None
        recebido = input_str(required=False)
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='exit'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_required_False(self, fake_out):
        esperado = 'exit'
        recebido = input_str(required=False, escape=['exit', 'saída'])
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='sair'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_sair_required_False(self, fake_out):
        esperado = 'sair'
        recebido = input_str(required=False, escape=['exit', 'sair'])
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='sair'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_escape_exit_sair_required_False(self, fake_out):
        esperado = 'sair'
        recebido = input_str(required=False, escape=['exit', 'sair'])
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='3'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_positive_123_required_False(self, fake_out):
        esperado = '3'
        recebido = input_str(required=False, allowed=range(1, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='-3'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_negative_123_required_False(self, fake_out):
        esperado = '-3'
        recebido = input_str(required=False, allowed=range(-10, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(return_value='0'))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_with_valid_integers_required_False(self, fake_out):
        esperado = '0'
        recebido = input_str(required=False, allowed=range(-10, 5))
        self.assertEqual(recebido, esperado)

    @patch(target="builtins.input", new=Mock(side_effect=['123', '3']))
    @patch(target="sys.stdout", new_callable=StringIO)
    def test_input_allowed_with_invalid_integers_required_False(self, fake_out):
        input_str(required=False, allowed=range(-10, 5))
        esperado = error("Insira uma entrada válida.")
        recebido = fake_out.getvalue().strip()
        self.assertEqual(recebido, esperado)


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
