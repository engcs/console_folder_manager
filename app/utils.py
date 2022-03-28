import os
import shutil
from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
init()


def title(text):
    result = Figlet()
    return result.renderText(text)

def error(msg):
    return Fore.RED + "[Error] " + Style.RESET_ALL + msg


def input_int(text="", required=True, allowed=[], escape=[]):

    if allowed:
        for item in allowed:
            try:
                int(str(item))
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
    while True:
        try:
            result = input(text).strip()
            if result == "":
                if not required:
                    return None
                else:
                    raise TypeError("Error. The field is required.")
            if escape:
                if result in escape:
                    return result
            if allowed:
                if result not in allowed:
                    raise ValueError("Error. The value is not allowed.")
        except TypeError:
            print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Error! A entrada não é válida. Tente novamente." + Style.RESET_ALL)
        else:
            return result



# def input_str_with_exit(text="", required=True):
#     while True:
#         try:
#             result = input(text).strip()
#             if result == "":
#                 if required is False:
#                     return None
#                 else:
#                     raise TypeError("Error. The field is required.")
#             elif result == "exit":
#                 return result
#         except TypeError:
#             print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
#         else:
#             return result


def get_dirs():
    START = "CLT"
    clt_dir = []
    for dir in os.listdir():
        if os.path.isdir(dir):
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

