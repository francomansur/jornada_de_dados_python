"""Exercício 05 Aula 07 Jornada de Dados Python."""


def calcular_desvio_padrao(lista_valores: list[float]) -> float:
    """Calcula Desvio Padrão de uma Lista."""
    n = len(lista_valores)
    media = sum(lista_valores) / n
    soma = 0
    for x in lista_valores:
        soma += (x - media) ** 2
    variancia = soma / (n - 1)
    desvio_p = variancia**0.5
    return desvio_p


lista_valores = [10, 12, 23, 23, 16, 23, 21, 16]
print(f"\nValores: {lista_valores}")
print(f"Desvio Padrão: {round(calcular_desvio_padrao(lista_valores), 2)}\n")
