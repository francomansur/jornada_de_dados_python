"""Exercicio 01 Aula 07 Jornada de Dados."""


def calcular_media(lista: list[float]) -> float:
    """Calcula a média de valores em uma Lista."""
    return sum(lista) / len(lista)


lista = [102, 56.7, 45.8, 34, 67]
media = calcular_media(lista)
print(media)
