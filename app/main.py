import os
import yaml

from utils import *

APP_DIR = "app"
DETAILS_TEMPLATE = {'nome': '', 'endereco': '', 'telefone': '', 'número': ''}
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
    print("")
    os.system('PAUSE')


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
    dirs = get_dirs(path)
    if dirs:
        print(dirs)
    else:
        print(error("Não há nenhum diretório aqui!"))
    return dirs


def get_last_id_folder(path):
    dirs = list_dirs(path)
    print("")
    if dirs:
        last_dir = dirs[-1]
        id_last_dir = int(last_dir[-4:])
        next_id_dir = id_last_dir + 1
    else:
        next_id_dir = 0
    return next_id_dir


def create_dir(path):
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


def get_details(path, dir_name):
    try:
        file_name = "details.yaml"
        fullpath = os.path.join(path, dir_name, file_name)

        with open(file=fullpath, encoding='utf8') as file:
            details = yaml.load(file, Loader=yaml.FullLoader)
            return details
    except FileNotFoundError as e:
        print(error(f"Não existe um arquivo 'details.yaml'"
                    f" na pasta '{fullpath}'."))
        return
    except PermissionError as e:
        print(e)
        return


def view_details(path):
    while True:
        raw = input_int(f"Número da pasta a ser visualizada"
                        f" ou deixe em branco para voltar: ",
                        required=False)

        if raw is None:
            return

        id_dir = raw
        dir_name = f"CLT{id_dir:04d}"

        if dir_name not in get_dirs(path):
            print(error(f"A pasta {dir_name} não existe."))
            continue

        details = get_details(path, dir_name)
        if details:
            print(details)
            print("")
            os.system('PAUSE')
            return


def edit_details(path):
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
            dict_file = DETAILS_TEMPLATE
            create_yaml(details_path, dict_file)
            print(f"Um arquivo de detalhes foi criado em {dir_name}.")

        if dir_name in get_dirs(path):
            call_editor(path, dir_name)
            return


def create_yaml(path, data):
    with open(file=path, mode='w', encoding='utf8') as file:
        yaml.dump(data, file, allow_unicode=True, encoding='utf-8')


def call_editor(path, dir_name):
    file_name = "details.yaml"
    fullpath = os.path.join(path, dir_name, file_name)
    os.system(f"notepad '{fullpath}'")


def delete_dir(path):
    yes_or_no = input_str(
        f"Deseja exibir os diretórios existentes (y/n)? ",
        allowed=['y', 'n'],
        required=True)

    if yes_or_no == 'y':
        list_dirs(path)
        print("")

    while True:
        raw = input_int(f"Número da pasta a ser removida ou 'exit'"
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
                    list_dirs(path)
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
