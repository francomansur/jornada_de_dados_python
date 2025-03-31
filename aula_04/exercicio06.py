"""    
    Exercício 6: Eliminação de Duplicatas
    Dada uma lista de emails, remover todos os duplicados.
"""

print('')

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)