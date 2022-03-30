import os
import shutil
import stat

import yaml
from colorama import Back, Fore, Style, init
from pyfiglet import Figlet

init()


def title(text):
    result = Figlet()
    return result.renderText(text)


def error(msg):
    return Fore.RED + "[Error] " + Style.RESET_ALL + msg


def warning(msg):
    return Fore.YELLOW + "[Warning] " + Style.RESET_ALL + msg


def input_int(text="", required=True, allowed=[], escape=[]):

    if allowed:
        try:
            allowed = [int(str(item)) for item in allowed]
        except ValueError:
            raise ValueError("Error! Allowed values must be integers.")

    while True:
        try:
            raw = input(text).strip()
            if raw == "" and required:
                print(error("O campo é obrigatório."))
                continue
            if raw == "" and not required:
                return None
            if escape and raw in escape:
                return raw
            result = int(raw)
            if allowed and result not in allowed:
                print(error("Insira um valor válido."))
                continue
        except ValueError:
            print(error("O valor informado não é um número válido."))
        else:
            return result


def input_str(text="", required=True, allowed=[], escape=[]):

    if allowed:
        allowed = [str(item).lower() for item in allowed]

    while True:
        raw = input(text).strip().lower()
        if raw == "" and required:
            print(error("O campo é obrigatório."))
            continue
        if raw == "" and not required:
            return None
        if escape and raw in escape:
            return raw
        result = str(raw)
        if allowed and result not in allowed:
            print(error("Insira uma entrada válida."))
            continue
        return result


def check_if_dirs_exists(path):
    dirs = get_dirs(path)
    if not dirs:
        print(error("Não há nenhum diretório aqui!"))
        print("")
        os.system('PAUSE')
    return dirs


def get_dirs(path="/"):
    START = "CLT"
    clt_dir = []
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            if dir.startswith(START):
                clt_dir.append(dir)
    if clt_dir:
        clt_dir.sort()
        return clt_dir
    else:
        return None


def get_last_id_folder(path):
    dirs = get_dirs(path)
    if dirs:
        last_dir = dirs[-1]
        id_last_dir = int(last_dir[-4:])
        next_id_dir = id_last_dir + 1
    else:
        next_id_dir = 0
    return next_id_dir


def make_dir(path):
    try:
        os.mkdir(path)
        return path
    except FileExistsError as e:
        if e.winerror == 183:
            print(Fore.RED + f"A pasta {e.filename} já existe!" + Style.RESET_ALL)
        else:
            print(f"{type(e).__name__, e.__str__()}")


def create_yaml(path, data):
    with open(file=path, mode='w', encoding='utf8') as file:
        yaml.dump(data, file, allow_unicode=True, encoding='utf-8')


def get_details(path, dir_name):
    try:
        file_name = "details.yaml"
        fullpath = os.path.join(path, dir_name, file_name)

        with open(file=fullpath, encoding='utf8') as file:
            details = yaml.load(file, Loader=yaml.FullLoader)
            return details
    except FileNotFoundError as e:
        print(error(f"Não existe um arquivo 'details.yaml'"
                    f" na pasta '{dir_name}'."))
    except PermissionError as e:
        print(e)
        return

def call_editor(path, dir_name):
    file_name = "details.yaml"
    fullpath = os.path.join(path, dir_name, file_name)
    os.system(f"notepad '{fullpath}'")

def rm_dir(dir, path="/"):
    abs_path = os.path.join(path, dir)
    shutil.rmtree(abs_path, ignore_errors=False, onerror=remove_readonly)


def remove_readonly(func, path, exc_info):
    """
    https://bugs.python.org/msg357315
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error in folder (read only folder),
    it attempts to add write permission and then retries removal.

    Usage : ``shutil.rmtree(path, onerror=remove_readonly)``
    """
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)
