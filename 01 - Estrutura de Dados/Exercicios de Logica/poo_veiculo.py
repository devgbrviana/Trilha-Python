""""Descrição
Implemente uma classe Veiculo que represente um carro com marca, modelo e ano. Crie um método que verifique se o carro é considerado antigo (mais de 20 anos).

Entrada
Marca, modelo e ano do veículo.
Saída
"Veículo antigo" se o carro tiver mais de 20 anos.
"Veículo novo" caso contrário.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis."""



from datetime import datetime

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def verificar_antigo(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self.ano
        if idade > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"


marca = input()
modelo = input()
ano = int(input())

carro = Veiculo(marca, modelo, ano)
print(carro.verificar_antigo())
