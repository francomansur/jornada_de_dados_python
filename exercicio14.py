"""
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
"""

print('')

data = str(input('Digite uma data no formato "dd/mm/aaaa": '))

dia, mes, ano = data.split('/')

print(f'Dia: {dia}\nMês: {mes}\nAno: {ano}\n')