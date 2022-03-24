import os
import sys
from utils import *


def menu():

    menu_str = """
    1 : LISTAR DIRETÓRIOS [CLT]
    2 : CRIAR NOVA PASTA [CLT]
    3 : VISUALIZAR DETALHES
    4 : EDITAR DETALHES
    0 : SAIR
    """

    while True:
        os.system('CLS')
        print(title("MEU GESTOR"))
        print("Escolha uma opção numérica ou digite 'exit' para sair:\n")
        print(menu_str)
        choice = input_int_with_exit("Entre com sua escolha: ")
        if choice == 1:                     # LISTAR DIRETÓRIOS [CLT]
            print(f"Opção {choice}")
            list_dirs()
            os.system('PAUSE')
        elif choice == 2:                   # CRIAR NOVA PASTA [CLT]
            print(f"Opção {choice}")
            create_dir()
            os.system('PAUSE')
        elif choice == 3:                   # VISUALIZAR DETALHES
            print(f"Opção {choice}")
            view_details()
            os.system('PAUSE')
        elif choice == 4:                   # EDITAR DETALHES
            print(f"Opção {choice}")
            edit_details()
            os.system('PAUSE')
        elif choice == 0 or choice == 'exit': # SAIR
            exit()


def list_dirs():
    pass


def create_dir():
    pass


def view_details():
    pass


def edit_details():
    pass


def main():
    menu()
    os.system('PAUSE')


if __name__ == "__main__":
    main()
