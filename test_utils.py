# https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
# https://andressa.dev/2019-07-20-using-pach-to-test-inputs/

import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from utils import *


class MyTestCase(unittest.TestCase):
    def test_input_str(self):
        with patch("builtins.input", side_effect=["", "teste"]), patch("sys.stdout", new=StringIO()) as fake_out:
            input_str()
            self.assertEqual(fake_out.getvalue().strip(), Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)


if __name__ == "__main__":
    unittest.main()


# def run_func_return_print(self, given_answer, expected_out, func, *args):
    #     with patch("builtins.input", return_value=given_answer), patch("sys.stdout", new=StringIO()) as fake_out:
    #         func(args)
    #         self.assertEqual(fake_out.getvalue().strip(), expected_out)
    #
    # def run_func_return_value(self, given_answer, expected_out, func, *args):
    #     with patch(target="builtins.input", return_value=given_answer) as fake_out:
    #         func(args)
    #         self.assertEqual(fake_out.return_value, expected_out)
    # #
    # # def test_meu_teste(self):
    # #     self.run_func_return_print('valor', 'valor', meu_teste)
    # #
    # def test_input_str(self):
    #     self.run_func_return_value(['valor', ''], 'valor', input_str)
    #
    # def test_input_number(self):
    #     self.run_func_return_value('123', '123', input_str)

    # @patch('utils.meu_teste', "builtins.input", side_effect=["teste", "titulo"])
    # def test_meu_teste(self, hello_world_patched):
    #     assert meu_teste("titulo") == "titulo"
    #     assert meu_teste("titulo") == "titulo"
    #     assert hello_world_patched.call_count == 2
    #     # with patch("builtins.input" ,return_value='') as fake_out:
    #     #     input_str("titulo", )
    #     #     self.assertEqual(fake_out.return_value, expected_out)

    # def test_blah(self):
    #     o = MagicMock()
    #
    #     o.foo.side_effect = ['teste1', 'teste2']
    #
    #     assert o.foo() == 'teste1'
    #     assert o.foo() == 'teste2'
