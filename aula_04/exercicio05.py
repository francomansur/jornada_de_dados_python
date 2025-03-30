"""    
    Exercício 5: Preço total da lista de compras
    Dada a lista ["maçã", "banana", "cereja"] 
    e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
    calcule o preço total da lista de compras.
"""

print('')

lista_produtos = ["maçã", "banana", "cereja"]
dicionario_produtos = {"maçã": 0.45, 
                       "banana": 0.30, 
                       "cereja": 0.65}

total = 0
for produtos in lista_produtos:
    total = total + dicionario_produtos[produtos]

print(f'Total: R${total}\n')