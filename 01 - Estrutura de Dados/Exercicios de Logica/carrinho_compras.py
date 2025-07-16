
#Descrição
#Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

#Entrada
#Lista de produtos adicionados ao carrinho (cada um com nome e preço).
#Saída
#Lista dos produtos adicionados e o total da compra.
#Exemplos
#A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

#Entrada	            Saída
#2                      Pão: R$3.50
#Pão 3.50               Leite: R$4.00
#Leite 4.00             Total: R$7.50


carrinho = []
total = 0.0

n = int(input().strip())

for _ in range(n):
    linha = input().strip()

    posicao_espaco = linha.rfind(" ")
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])

    carrinho.append((item, preco))
    total += preco

for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

print(f"Total: R${total:.2f}")
