"""Exercício 03 Aula 07 Jornada de Dados Python."""


def contar_valores_unicos(lista: list[int]) -> int:
    """Conta quantos valores únicos tem em uma lista."""
    return len(set(lista))


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]

resultado = contar_valores_unicos(lista)
print(resultado)
