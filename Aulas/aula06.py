## COLORAMA PARA IMPORTAR CORES NO TERMINAL!!

from colorama import Fore, Style, Back

print(Fore.RED + "Mensagem de erro" + Style.RESET_ALL)
print(Fore.GREEN + "Tudo certo!" + Style.RESET_ALL)
print(Back.RED + Fore.WHITE + " ALERTA: Algo deu errado! " + Style.RESET_ALL)
print(Back.GREEN + Fore.BLACK + " SUCESSO: Tudo certo! " + Style.RESET_ALL)
