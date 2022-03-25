import os
import sys
import shutil
from utils import *


def menu():

    menu_str = """
    1 : LISTAR DIRETÓRIOS [CLT]
    2 : CRIAR NOVA PASTA [CLT]
    3 : VISUALIZAR DETALHES
    4 : EDITAR DETALHES
    5 : DELETAR PASTA [CLT]
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
        elif choice == 5:                   # DELETAR PASTA [CLT]
            delete_dir()
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
    while True:
        raw = input_int_with_exit(f"Número da nova pasta ou 'exit' para sair [{next_id_dir:04d}]: ", required=False)
        if raw == 'exit':  # SAIR
            return
        elif raw is None:
            new_id_dir = next_id_dir
        else:
            new_id_dir = raw
        new_dir_name = f"CLT{new_id_dir:04d}"
        if make_dir(new_dir_name):
            print(f"A pasta {new_dir_name} foi criada com sucesso!")
            break
    os.system('PAUSE')


def view_details():
    pass


def edit_details():
    pass


def delete_dir():
    while True:
        raw = input_int_with_exit(f"Número da pasta a ser removida ou 'exit' para sair: ", required=True)
        if raw == 'exit':  # SAIR
            return
        else:
            id_dir = raw
            dir_name = f"CLT{id_dir:04d}"
            if dir_name in get_dirs():
                print(f"Tem certeza que deseja remover a pasta {dir_name}?")
                raw = input_str_with_exit(Fore.YELLOW + "Digite o nome completo da pasta para confirmar ou 'exit' para sair: " + Style.RESET_ALL)
                if raw == "exit":
                    return
                elif raw.upper() == dir_name.upper():
                    path = os.path.join(os.getcwd(), dir_name)
                    shutil.rmtree(path)
                    print(f"A pasta {dir_name} foi removida com sucesso!")
                else:
                    print(Fore.RED + "O nome está incorreto! Operação cancelada." + Style.RESET_ALL)
                break
            else:
                print(f"Não existe pasta com esse número!")
    os.system('PAUSE')


def main():
    menu()
    os.system('PAUSE')


if __name__ == "__main__":
    main()
