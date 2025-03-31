"""    
    Exercício 8: Ordenação Personalizada
    Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
"""

print('')

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Carol", "idade": 20},
    {"nome": "Bob", "idade": 25}
]

pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)