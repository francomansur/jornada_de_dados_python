"""    
    Exercício 7: Filtragem de Dados
    Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
"""

print('')

idades = [22, 15, 30, 17, 18]

idades_maior = [idade for idade in idades if idade >= 18]

print(f'Idades maior que 18: {idades_maior}\n')