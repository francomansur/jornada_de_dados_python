"""
Base 1: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

numeros = []

for x in range(5):
    while True:
        try:
            numeros.append(int(input("Digite um número inteiro: ")))
            break
        except ValueError:
            print("Número inválido.\n")

max = max(numeros)
min = min(numeros)

posicoes_max = [str(i) for i, n in enumerate(numeros) if n == max]
posicoes_min = [str(i) for i, n in enumerate(numeros) if n == min]

print(f'\nO maior valor digitado é {max}, nas posições: {"...".join(posicoes_max)}')
print(f'O maior valor digitado é {min}, nas posições: {"...".join(posicoes_min)}\n')
