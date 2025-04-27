"""
Exercício 13: Consumo de API Simulado
Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
"""

print("")

pagina_atual = 1
pagina_total = 5

while pagina_atual <= pagina_total:
    print(f"Pagina {pagina_atual}/{pagina_total} processada.")
    pagina_atual += 1

print("\nTodas as páginas foram processadas.\n")
