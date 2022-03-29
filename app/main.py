import os

from utils import *

DIR_APP = "app"

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
        elif choice == 0 or choice == 'exit': # SAIR
            exit()


def list_dirs():
    print("\n################# LISTAR DIRETÓRIOS [CLT] #################\n")
    dirs = get_dirs(DIR_APP)
    if dirs is None:
        print(Fore.RED + "Não há nenhum diretório aqui!" + Style.RESET_ALL)
    else:
        print(dirs)
    print()
    os.system('PAUSE')


def create_dir():
    print("\n################# CRIAR DIRETÓRIO [CLT] #################\n")
    dirs = get_dirs(DIR_APP)
    if dirs is None:
        last_dir = "CLT0000"
    else:
        last_dir = dirs[-1]
    id_last_dir = int(last_dir[-4:])
    next_id_dir = id_last_dir + 1
    while True:
        raw = input_int(f"Número da nova pasta ou 'exit' para sair [{next_id_dir:04d}]: ", required=False, escape=['exit'])
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
    print()
    os.system('PAUSE')


def view_details():
    print(input_str("Teste: ", required=True, allowed=['s', 'y'], escape='exit'))
    os.system('PAUSE')


def edit_details():
    print("\n#################  EDITAR DETALHES [CLT]  ##################\n")
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
    print("\n################# DELETAR DIRETÓRIO [CLT] ##################\n")
    yes_or_no = input_str(f"Deseja exibir os diretórios existentes (s/n)? ", required=True)
    if yes_or_no == 's':
        dirs = get_dirs()
        if dirs is None:
            print(Fore.RED + "Não há nenhum diretório aqui!" + Style.RESET_ALL)
        else:
            print(dirs)
        print()

    while True:
        raw = input_int(f"Número da pasta a ser removida ou 'exit' para sair: ", required=True, escape=['exit'])
        if raw == 'exit':  # SAIR
            return
        else:
            id_dir = raw
            dir_name = f"CLT{id_dir:04d}"
            if dir_name in get_dirs():
                print(f"Tem certeza que deseja remover a pasta {dir_name}?")
                raw = input_str(Fore.YELLOW + "Digite o nome completo da pasta para confirmar ou 'exit' para sair: " + Style.RESET_ALL, escape=['exit'])
                if raw == "exit":
                    return
                elif raw.upper() == dir_name.upper():
                    rm_dir(dir_name)
                    print(f"A pasta {dir_name} foi removida com sucesso!")
                else:
                    print(Fore.RED + "O nome está incorreto! Operação cancelada." + Style.RESET_ALL)
                break
            else:
                print(f"Não existe pasta com esse número!")
    print()
    os.system('PAUSE')


def main():
    menu()
    # print(input_int("Insira um número: ", allowed=[1.5, 1.6, 1.7], escape=['exit']))
    os.system('PAUSE')


if __name__ == "__main__":
    main()
