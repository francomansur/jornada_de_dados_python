"""    
    Exercício 15: Processamento de Dados com Condição de Parada
    Processar itens de uma lista até encontrar um valor específico que indica a parada.
"""

print('')

lista = [1,2,3,4,5,6,7,8,9,10]
tamanho_lista = len(lista)
i = 1  

while i <= tamanho_lista:  
    print(f'Elemento {i}/{tamanho_lista}')
    
    if lista[i - 1] == 8: 
        print('\nElemento encontrado!\n')
        break

    i += 1
