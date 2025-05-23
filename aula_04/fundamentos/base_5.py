"""
Base 4: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = []
numeros_pares = []
numeros_impares = []

while True:
    try:
        numero = input('Digite um número inteiro, ou "sair" para sair: ')

        if numero == "sair":
            break

        if int(numero) == 0:
            raise ValueError
        elif numero.isdigit():
            numeros.append(int(numero))
            if int(numero) % 2 == 0:
                numeros_pares.append(int(numero))
            else:
                numeros_impares.append(int(numero))

    except ValueError:
        print("Valor inválido\n")

print(f"\nNúmeros: {sorted(numeros)}")
print(f"Números pares: {sorted(numeros_pares)}")
print(f"Números ímpares: {sorted(numeros_impares)}\n")
