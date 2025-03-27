numeros = []

for x in range(5):
    while True:
        try:
            numeros.append(int(input('Digite um número inteiro: ')))
            break
        except ValueError:
            print('Número inválido.\n')

print(f'O maior valor digitado é {max(numeros)}, e o menor é {min(numeros)}.')
