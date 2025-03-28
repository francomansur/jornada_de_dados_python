"""    
    Exercício 1: Lista de números ao quadrado
    Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
"""

print('')

lista_quadrado = []

while True:
    try:
        for x in range(10):
            numero_quadrado = int((input('Digite um número inteiro: ')))
            lista_quadrado.append(numero_quadrado**2)
        break         
    except ValueError:
        print('Número inválido.')

print(f"\nLista dos números ao quadrado: {', '.join(str(n) for n in lista_quadrado)}\n")
