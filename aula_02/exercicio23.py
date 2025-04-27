"""
23. Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
"""

print("")

while True:
    try:
        numero_1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("O valor digitado não é um número.\n")

while True:
    try:
        numero_2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("O valor digitado não é um número.\n")

while True:
    try:
        operador = str(input("Digite o operador da conta (+, -, *, /): "))
        if operador == ("+"):
            resultado = numero_1 + numero_2
            print(f"{numero_1} {operador} {numero_2} = {resultado}\n")
            break
        elif operador == ("-"):
            resultado = numero_1 - numero_2
            print(f"{numero_1} {operador} {numero_2} = {resultado}\n")
            break
        elif operador == ("*"):
            resultado = numero_1 * numero_2
            print(f"{numero_1} {operador} {numero_2} = {resultado}\n")
            break
        elif operador == ("/"):
            resultado = numero_1 / numero_2
            print(f"{numero_1} {operador} {numero_2} = {resultado}\n")
            break
        else:
            raise ValueError
    except ValueError:
        print("Operador inválido.\n")
