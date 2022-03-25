from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
init()


def title(text):
    result = Figlet()
    return result.renderText(text)


def input_int(text="", required=True):
    while True:
        try:
            result = input(text).strip()
            if result == "":
                if required is False:
                    return None
                else:
                    raise TypeError("Error. The field is required.")
            result = int(result)
        except TypeError:
            print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Error! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)
        else:
            return result


def input_int_with_exit(text="", required=True):
    while True:
        try:
            result = input(text).strip()
            if result == "":
                if required is False:
                    return None
                else:
                    raise TypeError("Error. The field is required.")
            elif result == "exit":
                return None
            result = int(result)
        except TypeError:
            print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Error! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)
        else:
            return result


def input_str(text="", required=True):
    while True:
        try:
            result = input(text).strip()
            if result == "":
                if required is False:
                    return None
                else:
                    raise TypeError("Error. The field is required.")
        except TypeError:
            print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
        else:
            return result


def input_str_with_exit(text="", required=True):
    while True:
        try:
            result = input(text).strip()
            if result == "":
                if required is False:
                    return None
                else:
                    raise TypeError("Error. The field is required.")
            elif result == "exit":
                return None
        except TypeError:
            print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
        else:
            return result
