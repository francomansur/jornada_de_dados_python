"""
    13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
"""

print('')

frase = str(input('Digite uma frase: '))

print(f'Frase formatada sem espaços iniciais/finais: "{frase.strip()}".\n')