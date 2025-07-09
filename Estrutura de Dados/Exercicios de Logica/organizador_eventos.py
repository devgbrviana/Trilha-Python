#Descrição
#Uma empresa quer criar um organizador de eventos que divida os participantes em grupos de acordo com o tema escolhido.

#Entrada
#Lista de participantes e o tema escolhido por cada um.
#Saída
#Dicionário agrupando os participantes por tema.
#Exemplos
#A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

#Entrada	                       Saída
#3                                 Fotografia: Lucas, Carlos
#Lucas, Fotografia                 Viagem: Ana
# Ana, Viagem                                     
#Carlos, Fotografia                

eventos = {}

n = int(input().strip())

for _ in range(n):
    linha = input().strip()
    nome, tema = [x.strip() for x in linha.split(",")]
    
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(nome)

for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
