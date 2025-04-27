"""
Exercício 8: Filtragem de Dados Faltantes
Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
"""

print("")

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"},
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)
