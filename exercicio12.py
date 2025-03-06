print('')

while True:
    try:
        nome = str(input('Digite seu nome: '))
        if nome.replace(" ", "").isalpha():
            break
        else:
            raise ValueError
    except ValueError:
        print('Nome inválido.\n')

print(f'Nome em maiúsculo: {nome.upper()}.\n')