"""
Exercício 10: Agregação de Dados por Categoria
Dado um conjunto de registros de vendas, calcular o valor total de vendas por categoria.
"""

print("")

vendas = [
    {"produto": "computador", "categoria": "eletrônico", "valor": 1200},
    {"produto": "tablet", "categoria": "eletrônico", "valor": 600},
    {"produto": "startup enxuta", "categoria": "livro", "valor": 40},
    {"produto": "desinfetante", "categoria": "limpeza", "valor": 20},
]

vendas_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in vendas_categoria:
        vendas_categoria[categoria] += valor
    else:
        vendas_categoria[categoria] = valor

print("Valor total de vendas por categoria:\n")
for categoria, valor in vendas_categoria.items():
    print(f"{categoria}: R${valor}")

print("")
