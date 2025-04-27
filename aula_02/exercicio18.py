"""
18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
"""

print("")

while True:
    try:
        entrada = (
            input("Digite um valor Booleano (True ou False): ").strip().capitalize()
        )
        if entrada == "True":
            valor = True
        elif entrada == "False":
            valor = False
        else:
            raise ValueError
        break
    except ValueError:
        print("Digite um valor Booleano válido (True/False).\n")

resultado = not valor

print(f"O resultado do NOT lógico de {valor} é {resultado}.\n")
