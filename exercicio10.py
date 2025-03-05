print('')
while True:
    try:
        raio = float(input('Digite o raio do círculo: '))
        break
    except ValueError:
        print('O valor digitado não é um número.\n')

area = 3.1416 * (raio**2)

print(f'A área do círculo com raio de {raio} é {area:.2f}.\n')