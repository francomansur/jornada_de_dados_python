"""
Exercicio 2: Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT.
Os dados incluem medições de temperatura.
Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'"
"""

print("")

while True:
    try:
        temperatura = float(input("Digite a Temperatura em °C: "))
        break
    except ValueError:
        print("Temperatura inválida.\n")

if temperatura < 18:
    print("Temperatura Baixa\n")
elif (temperatura >= 18) and (temperatura <= 26):
    print("Temperatura Normal\n")
else:
    print("Temperatura Alta\n")
