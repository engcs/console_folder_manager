from pyfiglet import Figlet
from colorama import Fore, Back, Style


def title(text):
    result = Figlet()
    return result.renderText(text)


def input_int(text):
    while True:
        try:
            result = int(input(text))
        except ValueError:
            print("Erro! O valor informado não é um número. Tente novamente.")
        else:
            return result


def input_int_with_exit(text):
    while True:
        try:
            result = input(text)
            if result != "exit":
                result = int(result)
        except ValueError:
            print(Fore.RED + "Erro! O valor informado não é um número. Tente novamente." + Style.RESET_ALL)
        else:
            return result


def input_str(text, required=True):
    while True:
        result = input(text).strip()
        if result:
            return result
        elif result == "" and required is False:
            return None
        print("Error! O campo não pode ser branco. Tente novamente.")
