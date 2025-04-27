"""
17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
"""

print("")

while True:
    try:
        entrada = (
            input("Digite o primeiro valor Booleano (True ou False): ")
            .strip()
            .capitalize()
        )
        if entrada == "True":
            valor_1 = True
        elif entrada == "False":
            valor_1 = False
        else:
            raise ValueError
        break
    except ValueError:
        print("Digite um valor Booleano válido (True/False).\n")

while True:
    try:
        entrada = (
            input("Digite o segundo valor Booleano (True ou False): ")
            .strip()
            .capitalize()
        )
        if entrada == "True":
            valor_2 = True
        elif entrada == "False":
            valor_2 = False
        else:
            raise ValueError
        break
    except ValueError:
        print("Digite um valor Booleano válido (True/False).\n")

resultado = valor_1 or valor_2

print(f"O OR lógico entre {valor_1} e {valor_2} é {resultado}.\n")
