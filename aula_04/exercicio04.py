"""    
    Exercício 4: Contar ocorrências de caracteres
    Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
"""

print('')

contagem = {}
frase = input('Digite uma palavra/frase: ')

for letra in frase:
    contagem[letra] = contagem.get(letra, 0) +1

for letra, quantidade in contagem.items():
    print(f"{letra}: {quantidade}")

