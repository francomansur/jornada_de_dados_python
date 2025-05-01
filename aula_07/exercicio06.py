"""Exercício 06 Aula 07 Jornada de Dados Python."""


def encontrar_valores_ausentes(sequencia: list[float]) -> list[float]:
    """Encontrar Valores Ausentes em uma Sequência."""
    completo = set(range(min(sequencia), max(sequencia) + 1))
    ausentes = list(completo - set(sequencia))
    return ausentes


sequencia = [1, 2, 3, 4, 6, 7, 8, 9, 15, 20]
valores_ausentes = encontrar_valores_ausentes(sequencia)
print(f"\nValores: {sequencia}")
print(f"Valores Ausentes: {valores_ausentes}\n")
