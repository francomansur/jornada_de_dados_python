"""    
    Exercício 3: Informações de um livro
    Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
"""

print('')

livro = {
    'titulo': 'Startup Enxuta',
    'autor': 'Eric Ries',
    'ano_publicacao': 2011
}

print(f'Nome do Livro: {livro['titulo']}\nAutor do livro: {livro['autor']}\nAno de publicação: {livro['ano_publicacao']}\n')

# Poderia ser usado:
#
# for chave, valor in livro.items():
#   print(f"{chave}: {valor}")