import os
import sys
from utils import *


def menu():

    menu_str = """
    1 : LISTAR DIRETÓRIOS [CLT]
    2 : CRIAR NOVA PASTA [CLT]
    3 : RETORNAR DETALHES
    4 : CRIAR DETALHES
    0 : SAIR
    """

    while True:
        os.system('CLS')
        print(title("MEU GESTOR"))
        print("Escolha uma opção numérica ou digite 'exit' para sair:\n")
        print(menu_str)
        choice = input_int_with_exit("Entre com sua escolha: ")
        if choice == 1:
            print(f"Opção {choice}")
            os.system('PAUSE')
        elif choice == 2:
            print(f"Opção {choice}")
            os.system('PAUSE')
        elif choice == 3:
            print(f"Opção {choice}")
            os.system('PAUSE')
        elif choice == 4:
            print(f"Opção {choice}")
            os.system('PAUSE')
        elif choice == 0 or choice == 'exit':
            exit()


def main():
    menu()
    os.system('PAUSE')


if __name__ == "__main__":
    main()
