"""
Exercício 6: Contagem de Palavras em Textos
Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""

print("")

texto = str(input("Digite seu texto: "))

texto_palavras = texto.lower().split()
texto_count = {}

for palavra in texto_palavras:
    if palavra in texto_count:
        texto_count[palavra] += 1
    else:
        texto_count[palavra] = 1

print("\nContagem de palavras:")
for palavra, contagem in texto_count.items():
    print(f"{palavra}: {contagem}")

print("")
