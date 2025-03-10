"""    
    Exercício 1: Verificação de Qualidade de Dados
    Você está analisando um conjunto de dados de vendas e precisa garantir 
    que todos os registros tenham valores positivos para `quantidade` e `preço`. 
    Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
    forem positivos ou "Dados inválidos" caso contrário."
"""

print('')

while True:
    try:
        preco = float(input('Digite o valor do produto: '))
        break
    except ValueError:
        print('Digite um valor válido.\n')

while True:
    try:
        quantidade = int(input('Digite a quantidade do produto: '))
        break
    except ValueError:
        print('Digite um valor válido.\n')

if (preco > 0) and (quantidade > 0):
    print('Dados Válidos')
else:
    print('Dados Inválidos\n')