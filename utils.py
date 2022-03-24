from pyfiglet import Figlet
from colorama import init, Fore, Back, Style
init()


def title(text):
    result = Figlet()
    return result.renderText(text)


def input_int(text, required=False):
    while True:
        try:
            result = input(text).strip()
            if result == "":
                if required is False:
                    return None
                else:
                    raise TypeError("Sorry, no numbers below zero")
            else:
                result = int(result)
        except ValueError:
            print(Fore.RED + "Erro! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)
        except TypeError:
            print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
        else:
            return result


def input_int_with_exit(text, required=True):
    while True:
        try:
            result = input(text).strip()
            if result == "":
                if required is False:
                    return None
                else:
                    raise TypeError("Sorry, no numbers below zero")
            elif result != "exit":
                result = int(result)
        except ValueError:
            print(Fore.RED + "Erro! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)
        except TypeError:
            print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)
        else:
            return result


def input_str(text, required=True):
    while True:
        result = input(text).strip()
        if result:
            return result
        elif result == "" and required is False:
            return None
        print(Fore.RED + "Error! O campo não pode ser branco. Tente novamente." + Style.RESET_ALL)

