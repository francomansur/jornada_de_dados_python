"""
24. Escreva um programa que solicite ao usuário para digitar um número.
    Classifique o número como positivo, negativo ou 0.
    Identifique se o número é par ou ímpar.
"""

print("")

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero > 0:
            print("O número é Positivo.")
        elif numero < 0:
            print("O número é Negativo.")
        else:
            print("O número é Igual a 0.")

        if numero % 2 == 0:
            print("O número é Par.\n")
            break
        else:
            print("O número é Ímpar.\n")
            break

    except ValueError:
        print("Número inválido.\n")
