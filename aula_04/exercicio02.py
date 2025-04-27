"""
Exercício 2: Modificar lista de linguagens
Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
"""

print("")

lista = ["Python", "Java", "C++", "JavaScript"]
print(f"\nLista antes: {lista}")

lista.remove("C++")
lista.append("Ruby")

print(f"Lista depois: {lista}\n")
