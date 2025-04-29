"""Exercício 02 Aula 07 Jornada de Dados."""


def filtrar_acima_de(valores: list[float], limite: float) -> list[float]:
    """Filtra valores de uma lista com base no limite inserido."""
    valores_abaixo = []
    for valor in valores:
        if valor <= limite:
            valores_abaixo.append(valor)
    return valores_abaixo


valores = [10, 10.5, 20, 30, 40, 50, 60, 70, 80, 90, 100]
limite = 60

lista_filtrada = filtrar_acima_de(valores, limite)
print(lista_filtrada)
