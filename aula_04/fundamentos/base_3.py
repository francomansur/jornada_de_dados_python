"""    
    Crie um programa onde o usuário possa digitar cinco valores numéricos.
    Cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
    No final, mostre a lista ordenada na tela.
"""

numeros = []

for _ in range(5):
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
            
            if not numeros:
                numeros.append(numero)
                print(f'Número {numero} adicionado na posicão 1.\n')
                break

            for i, n in enumerate(numeros):
                if numero < n:
                    numeros.insert(i, numero)
                    print(f'Número {numero} adicionado na posicão {i}\n')
                    break
            else:
                numeros.append(numero)
                print(f'Número {numero} adicionado na posicão {len(numeros)}\n')
            break
        except ValueError:
            print('Valor inválido.\n')

print(numeros)
