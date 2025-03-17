"""    
    Exercício 11: Leitura de Dados até Flag
    Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
"""

print('')

entrada = ''
while entrada.lower() != 'sair':
    entrada = input('Digite um valor (Ou "sair" para terminar): ')

print('')