"""
Base 6:  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

abre = []
fecha = []

while True:
    try:
        frase_1 = input("\nDigite uma expressão com parênteses (): ")

        if "(" in frase_1 or ")" in frase_1:
            break
        else:
            raise ValueError

    except ValueError:
        print("A expressão deve conter parênteses.")

for x in frase_1:
    if x == "(":
        abre.append(x)
    elif x == ")":
        fecha.append(x)

if (len(abre)) != (len(fecha)):
    print("\nExpressão inválida.\n")
else:
    print("\nExpressão válida.\n")
