while True:
    try:
        valor_1 = int(input('Digite um valor: '))
        break
    except ValueError:
        print('')
        print('Digite um valor numérico válido.\n')

valor_final = valor_1 %5
print(f'O resto da divisão de {valor_1} dividido por 5 é {valor_final}\n')
