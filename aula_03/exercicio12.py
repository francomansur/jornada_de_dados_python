"""    
    Exercício 12: Validação de Entrada
    Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
"""

print('')

numero = -1

while (numero < 0) or (numero > 50):
    try:
        numero = int(input('Digite um número inteiro entre 0 e 50: '))
    except ValueError:
        print('Número inválido.\n')
        numero = -1

print('\nNúmero válido.\n')