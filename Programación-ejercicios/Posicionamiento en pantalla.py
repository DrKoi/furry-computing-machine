import os
from colorama import init, Back, Fore
init()
def colorBACK():
  print(Back.RED + Fore.LIGHTYELLOW_EX, end="")
  os.system("cls")

print(Back.BLUE + Fore.LIGHTWHITE_EX, end="")
print("HOLA MUNDO")

print(Back.GREEN + Fore.LIGHTYELLOW_EX, end="")
input("Presione ENTER para continuar")
