import os

from utils import *

APP_DIR = "app"


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
    list_dirs(APP_DIR)
    print("")
    os.system('PAUSE')


# CRIAR NOVA PASTA [CLT]
def choice_2():
    print("\n##################  CRIAR DIRETÓRIO [CLT] ##################\n")
    create_dir()
    print("")


# VISUALIZAR DETALHES
def choice_3():
    print("\n###############  VISUALIZAR DETALHES [CLT]  ################\n")
    os.system('PAUSE')


# EDITAR DETALHES
def choice_4():
    print("\n#################  EDITAR DETALHES [CLT]  ##################\n")
    os.system('PAUSE')


# DELETAR PASTA [CLT]
def choice_5():
    print("\n################# DELETAR DIRETÓRIO [CLT] ##################\n")
    delete_dir()


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


def get_last_id_folder():
    dirs = list_dirs(APP_DIR)
    print("")
    if dirs:
        last_dir = dirs[-1]
        id_last_dir = int(last_dir[-4:])
        next_id_dir = id_last_dir + 1
    else:
        next_id_dir = 0
    return next_id_dir


def create_dir():
    next_id_dir = get_last_id_folder()
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

        if make_dir(os.path.join(APP_DIR, new_dir_name)):
            print(f"\nA pasta {new_dir_name} foi criada com sucesso!")
            list_dirs(APP_DIR)
            print("")
            os.system('PAUSE')
            break


def view_details():
    print(input_str("Teste: ", required=True, allowed=['s', 'y'], escape='exit'))
    os.system('PAUSE')


def edit_details():
    while True:
        raw = input_int(f"Número da pasta a ser editada ou 'exit' para sair: ", required=True, escape=['exit'])
        if raw == 'exit':  # SAIR
            return
        else:
            id_dir = raw
            dir_name = f"CLT{id_dir:04d}"
            if dir_name in get_dirs():
                yaml_path = os.path.join(dir_name, 'details.yaml')
                have_details = os.path.isfile(yaml_path)
                if have_details:
                    print("POSSUI DETALHES")
                else:
                    print("NÃO POSSUI DETALHES")
                    yes_or_no = input_str(f"Deseja criar o arquivo 'details.yaml' (s/n)? ", required=True)
                    if yes_or_no == 's':
                        print("cria arquivo")
                        with open(yaml_path, "w") as file:
                            file.write("Delete me!")
                    else:
                        return


def delete_dir():
    yes_or_no = input_str(
        f"Deseja exibir os diretórios existentes (y/n)? ",
        allowed=['y', 'n'],
        required=True)

    if yes_or_no == 'y':
        list_dirs(APP_DIR)
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

        if dir_name in get_dirs(APP_DIR):
            print(f"\nTem certeza que deseja remover a pasta {dir_name}?")

            raw = input_str(warning("Digite o nome completo da pasta para"
                                    " confirmar ou 'exit' para sair: "),
                            escape=['exit'])

            if raw == "exit":
                return

            if raw.upper() == dir_name.upper():
                rm_dir(dir_name, APP_DIR)
                print(f"\nA pasta {dir_name} foi removida com sucesso!")
                list_dirs(APP_DIR)
                print("")
            else:
                print(error("O nome está incorreto! Operação cancelada."))
            break

        else:
            print(f"Não existe pasta com esse número!")
    os.system('PAUSE')

def main():
    menu()
    os.system('PAUSE')


if __name__ == "__main__":
    main()
