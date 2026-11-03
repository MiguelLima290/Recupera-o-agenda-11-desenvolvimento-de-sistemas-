# Controle de níveis de água
from colorama import Fore, Style, init

init()

# lista com as mensagens de cada nível
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)",
]


# função que escolhe a cor de acordo com o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE


print("Monitoramento do reservatório\n")

# simulação com os 5 níveis
for i in range(len(niveis)):
    cor = definir_cor(i + 1)
    print(cor + niveis[i])

# volta o terminal ao estilo padrão
print(Style.RESET_ALL)
