"""
22. Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
"""

print("")

while True:
    try:
        palavra = str(input("Digite uma palavra: ")).strip()
        break
    except ValueError:
        print("Você não digitou uma palavra.\n")

palindromo = palavra == palavra[::-1]

print(f"Palíndromo: {palindromo}\n")
