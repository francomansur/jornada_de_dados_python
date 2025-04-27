"""
25. Crie um script que solicite ao usuário uma lista de números separados por vírgula.
O programa deve converter a string de entrada em uma lista de números inteiros.
"""

print("")

while True:
    try:
        numeros = input(
            'Digite uma lista de números inteiros separados por ","\nExemplo: 10, 64, 42, 16\nNúmeros: '
        )

        lista_str = numeros.split(",")

        for num in lista_str:
            if not num.strip().isdigit():
                raise ValueError

        numeros_int = []
        for num in lista_str:
            numeros_int.append(int(num.strip()))

        print(f"Lista de números inteiros: {numeros_int}\n")
        break

    except ValueError:
        print("Valores inválidos.\n")
