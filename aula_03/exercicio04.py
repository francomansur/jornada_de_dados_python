"""    
    Exercício 4:
    Antes de processar os dados de usuários em um sistema de recomendação, 
    você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
    Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.
"""

print('')

while True:
    try:
        idade = int(input('Digite sua idade: '))
        break
    except ValueError:
        print('Idade Inválida\n')

while True:
    try:
        email = str(input('Digite seu email: '))
        if '@' not in email or "." not in email:
            raise ValueError
        break
    except ValueError:
        print('Email Inválido\n')

if (idade >= 18) and (idade <= 65):
    print('\nDados de usuário válidos.\n')
else:
    print('\nDados de usuário inválidos. Idade requerida: 18 a 65 anos.\n')