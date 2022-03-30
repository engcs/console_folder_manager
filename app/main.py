import os

import yaml
from utils import *

DETAILS_TEMPLATE = {'nome': '', 'endereco': '', 'contato': '', 'pessoa': ''}
CURRENT_WORKING_PATH = os.getcwd()


def menu():
    menu_str = """
    1 : LISTAR DIRETÓRIOS [CLT]
    2 : CRIAR NOVA PASTA [CLT]
    3 : VISUALIZAR DETALHES
    4 : EDITAR DETALHES
    5 : DELETAR PASTA [CLT]
    0 : SAIR"""

    os.system('CLS')
    print(title("MEU GESTOR"))

    while True:
        print("\nEscolha uma opção numérica ou digite 'exit' para sair:")
        print(menu_str)
        choice = input_int("\nEntre com sua escolha: ", escape=['exit'])
        if choice == 1:  # LISTAR DIRETÓRIOS [CLT]
            choice_1()
        elif choice == 2:  # CRIAR NOVA PASTA [CLT]
            choice_2()
        elif choice == 3:  # VISUALIZAR DETALHES
            choice_3()
        elif choice == 4:  # EDITAR DETALHES
            choice_4()
        elif choice == 5:  # DELETAR PASTA [CLT]
            choice_5()
        elif choice == 0 or choice == 'exit':  # SAIR
            choice_0()


# SAIR
def choice_0():
    exit()


# LISTAR DIRETÓRIOS [CLT]
def choice_1():
    print("\n#################  LISTAR DIRETÓRIOS [CLT] #################\n")
    list_dirs(CURRENT_WORKING_PATH)


# CRIAR NOVA PASTA [CLT]
def choice_2():
    print("\n##################  CRIAR DIRETÓRIO [CLT] ##################\n")
    create_dir(CURRENT_WORKING_PATH)
    print("")


# VISUALIZAR DETALHES
def choice_3():
    print("\n###############  VISUALIZAR DETALHES [CLT]  ################\n")
    view_details(CURRENT_WORKING_PATH)


# EDITAR DETALHES
def choice_4():
    print("\n#################  EDITAR DETALHES [CLT]  ##################\n")
    edit_details(CURRENT_WORKING_PATH)


# DELETAR PASTA [CLT]
def choice_5():
    print("\n################# DELETAR DIRETÓRIO [CLT] ##################\n")
    delete_dir(CURRENT_WORKING_PATH)


#############################################################################
#                      [        FUNÇÕES        ]                            #
#############################################################################

def list_dirs(path="/"):
    dirs = check_if_dirs_exists(path)
    if dirs:
        return dirs


def create_dir(path="/"):
    next_id_dir = get_last_id_folder(path)
    while True:
        raw = input_int(
            f"Número da nova pasta ou 'exit' para sair [{next_id_dir:04d}]: ",
            required=False,
            escape=['exit'])

        if raw == 'exit':
            return

        if raw is None:
            new_id_dir = next_id_dir
        else:
            new_id_dir = raw

        new_dir_name = f"CLT{new_id_dir:04d}"

        if make_dir(os.path.join(path, new_dir_name)):
            print(f"\nA pasta {new_dir_name} foi criada com sucesso!")
            list_dirs(path)
            print("")
            os.system('PAUSE')
            break


def view_details(path="/"):
    if not check_if_dirs_exists(path):
        return

    while True:
        raw = input_int(f"Número da pasta a ser visualizada"
                        f" ou deixe em branco para voltar: ",
                        required=False)

        if raw is None:
            return

        id_dir = raw
        dir_name = f"CLT{id_dir:04d}"

        if not get_dirs(path):
            print("Não há pastas aqui")
            return

        if dir_name not in get_dirs(path):
            print(error(f"A pasta {dir_name} não existe."))
            continue

        details = get_details(path, dir_name)
        if details:
            print(details)
        print("")


def edit_details(path="/"):
    if not check_if_dirs_exists(path):
        return

    while True:
        raw = input_int(f"Número da pasta a ser editada"
                        f" ou deixe em branco para voltar: ",
                        required=False)

        if raw is None:
            return

        id_dir = raw
        dir_name = f"CLT{id_dir:04d}"

        if dir_name not in get_dirs(path):
            print(error(f"A pasta {dir_name} não existe."))
            continue

        details_name = 'details.yaml'
        details_path = os.path.join(path, dir_name, details_name)
        have_details = os.path.isfile(details_path)
        if not have_details:

            raw = input_str("Deseja criar um arquivo de detalhes (y/n)? ",
                            allowed=['y', 'n'])

            if raw == 'y':
                dict_file = DETAILS_TEMPLATE
                create_yaml(details_path, dict_file)
                print(f"Um arquivo de detalhes foi criado em {dir_name}.")
            elif raw == 'n':
                return

        if dir_name in get_dirs(path):
            call_editor(path, dir_name)
            return


def delete_dir(path="/"):
    check_if_dirs_exists(path)

    yes_or_no = input_str(
        f"Deseja exibir os diretórios existentes (y/n)? ",
        allowed=['y', 'n'],
        required=True)

    if yes_or_no == 'y':
        list_dirs(path)
        print("")

    while True:
        raw = input_int(f"Número da pasta a ser removida ou 'exit' "
                        f"para sair: ",
                        required=True,
                        escape=['exit'])

        if raw == 'exit':
            return

        id_dir = raw
        dir_name = f"CLT{id_dir:04d}"

        if not get_dirs(path):
            print("Não há pastas neste diretório")
            return

        if dir_name in get_dirs(path):
            print(f"\nTem certeza que deseja remover a pasta {dir_name}?")

            raw = input_str(warning("Digite o nome completo da pasta para"
                                    " confirmar ou 'exit' para sair: "),
                            escape=['exit'])

            if raw == "exit":
                return

            if raw.upper() == dir_name.upper():
                try:
                    rm_dir(dir_name, path)
                # PermissionError: [WinError 5] Acesso negado
                except PermissionError as e:
                    print(e)
                else:
                    print(f"\nA pasta {dir_name} foi removida com sucesso!")
                    list_dirs(path) # se não houver mais pastas, não é pra dar erro
                    print("")
            else:
                print(error("O nome está incorreto! Operação cancelada."))
            break

        else:
            print(error(f"Não existe pasta com esse número!"))
    os.system('PAUSE')


def main():
    menu()
    os.system('PAUSE')


if __name__ == "__main__":
    main()
