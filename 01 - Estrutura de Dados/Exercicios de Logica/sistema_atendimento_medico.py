"""Descrição
Uma clínica médica quer automatizar seu sistema de atendimento. Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.

Critérios de Prioridade:

Pacientes acima de 60 anos têm prioridade.
Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
Os demais pacientes são atendidos por ordem de chegada.
Entrada
Um número inteiro n, representando a quantidade de pacientes.
n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
nome: string representando o nome do paciente.
idade: número inteiro representando a idade do paciente.
status: string que pode ser "urgente" ou "normal".
Saída
A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	                   Saída
3                          Ordem de Atendimento: Bruno, Ana, CarlosOrdem de Atendimento: Bruno, Ana, Carlos
Carlos, 40, normal
Ana, 70, normal
Bruno, 30, urgente
"""

def organizar_atendimento():
    n = int(input())
    pacientes = []

    for ordem_chegada in range(n):
        entrada = input().strip()
        nome, idade, status = map(str.strip, entrada.split(','))
        idade = int(idade)

        
        if status.lower() == "urgente":
            prioridade = 0
            chave_extra = -idade 
        elif idade >= 60:
            prioridade = 1
            chave_extra = -idade
        else:
            prioridade = 2
            chave_extra = ordem_chegada

        
        pacientes.append((prioridade, chave_extra, ordem_chegada, nome))

    pacientes.sort()

    ordem = [p[3] for p in pacientes]

    print("Ordem de Atendimento:", ", ".join(ordem))

organizar_atendimento()