"""Exercício 04 Aula 07 Jornada de Dados Python."""


def converter_celsius_para_fahrenheit(lista_celsius: list[float]) -> list[float]:
    """Converte uma lista de temperaturas em celsius para fahrenheit."""
    fahrenheit = [round((9 / 5) * temperatura + 32, 2) for temperatura in lista_celsius]
    return fahrenheit


temperaturas_celsius = [
    15.2,
    18.5,
    21.0,
    23.3,
    26.7,
    30.0,
    32.5,
    28.4,
    24.1,
    19.8,
    16.3,
    12.0,
]
temperaturas_fahrenheit = converter_celsius_para_fahrenheit(temperaturas_celsius)
print(temperaturas_fahrenheit)
