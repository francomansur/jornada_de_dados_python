"""
Base 4: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A: Quantos números foram digitados.
B: A lista de valores, ordenada de forma decrescente.
C: Se o valor 5 foi digitado e está ou não na lista.
"""

numeros = []

while True:
    try:
        numero = input('Digite um número inteiro, ou "sair" para sair: ')

        if numero == "sair":
            print("")
            break

        elif numero.isdigit():
            numeros.append(int(numero))

        else:
            raise ValueError

    except ValueError:
        print("Valor inválido\n")

print(f"Total de valores digitados: {len(numeros)}")
print(f"Lista dos valores em ordem decrescente: {sorted(numeros, reverse=True)}")

if 5 in numeros:
    print("A lista contém o número 5.\n")
else:
    print("A lista não contém o número 5.\n")
