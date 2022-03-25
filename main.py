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
            list_dirs()
        elif choice == 2:                   # CRIAR NOVA PASTA [CLT]
            create_dir()
        elif choice == 3:                   # VISUALIZAR DETALHES
            view_details()
        elif choice == 4:                   # EDITAR DETALHES
            edit_details()
        elif choice == 0 or choice is 'exit': # SAIR
            exit()


def list_dirs():
    print("\n### LISTAR DIRETÓRIOS [CLT] ###")
    dirs = get_dirs()
    if dirs is None:
        print(Fore.RED + "Não há nenhum diretório aqui!" + Style.RESET_ALL)
    else:
        print(dirs)
    os.system('PAUSE')


def create_dir():
    dirs = get_dirs()
    if dirs is None:
        last_dir = "CLT0000"
    else:
        last_dir = dirs[-1]
    id_last_dir = int(last_dir[-4:])
    next_id_dir = id_last_dir + 1
    choice = input_int_with_exit(f"Número da nova pasta [{next_id_dir:04d}]: ", required=False)
    if choice is None:
        print("Vazio")
    elif choice == 'exit':  # SAIR
        return
    os.system('PAUSE')


def view_details():
    pass


def edit_details():
    pass


def main():
    menu()
    os.system('PAUSE')


if __name__ == "__main__":
    main()
