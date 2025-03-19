"""    
    Exercício 14: Tentativas de Conexão
    Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
"""

# import requests

print('')

tentativas_maximas = 5
tentativa = 1
url = 'https://www.google.com'

while tentativa <= tentativas_maximas:
    print(f'Tentativa {tentativa}/{tentativas_maximas}')
    # try:
    #    resposta = requests.get(url, timeout=5)
    #    if resposta.status_code == 200:
    #       print("Conexão bem-sucedida!")
    #        break
    # except requests.RequestException as e:
    #    print(f"Erro na conexão: {e}")
    
    tentativa += 1

else:
    print('\nFalha ao conectar após várias tentativas.\n')
