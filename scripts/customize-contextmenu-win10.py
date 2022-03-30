####################################################
### THIS SCRIPT NEEDS ADMIN PERMISSION TO RUN !! ###
####################################################

import os
import sys
import winreg as reg

# Script file name
script_name = "main.py"

# Script path
script_path = os.path.join("app", script_name)

# Get path of current working directory
cwd = os.getcwd()

# Get path of python.exe (with console) and optional pythonw.exe (hidden console)
python_with_console = sys.executable
python_hidden_console = python_with_console.replace("python.exe", "pythonw.exe")

# Name of main key (head). Cannot contain spaces!
name_of_main_key = 'Meu_Gestor'

# Set the path of the key of context-menu in Windows 10, to clicking in a empty place in folder
key_path = fr"Directory\\Background\\shell\\{name_of_main_key}"

title_in_context_menu = "Meu Gestor (aqui)"

# Create the main key (head)
main_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(main_key, '', reg.REG_SZ, f'&{title_in_context_menu}')

# Create the subkey (inner key)
subkey = reg.CreateKey(main_key, r"command")
reg.SetValue(subkey, '', reg.REG_SZ, python_with_console + f' "{cwd}\\{script_path}"')
# reg.SetValue(subkey, '', reg.REG_SZ, python_hidden_console + f' "{cwd}\\{script_path}"')

