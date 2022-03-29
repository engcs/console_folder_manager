import os
import shutil

from colorama import Back, Fore, Style, init
from pyfiglet import Figlet

init()


def title(text):
    result = Figlet()
    return result.renderText(text)


def error(msg):
    return Fore.RED + "[Error] " + Style.RESET_ALL + msg


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
        allowed = [str(item) for item in allowed]

    while True:
        raw = input(text).strip()
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


def get_dirs(path):
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


def make_dir(path):
    try:
        os.mkdir(path)
        return path
    except FileExistsError as e:
        if e.winerror == 183:
            print(Fore.RED + f"A pasta {e.filename} já existe!" + Style.RESET_ALL)
        else:
            print(f"{type(e).__name__, e.__str__()}")


def rm_dir(path):
    abs_path = os.path.join(os.getcwd(), path)
    shutil.rmtree(abs_path)


