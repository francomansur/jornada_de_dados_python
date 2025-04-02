"""    
    Exercício 10: Divisão de Dados em Grupos
    Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
"""

print('')

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

par = [numero for numero in valores if numero % 2 == 0]
impar = [numero for numero in valores if numero % 2 != 0]

print(f'Números pares: {par}\nNúmeros ímpares: {impar}\n')