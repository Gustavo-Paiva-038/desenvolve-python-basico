#Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. 
# O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. 
# Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos 
# comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
# Cada entrada de dados tem uma mensagem indicando o dado solicitado 
# (mensagens em itálico, dado de entrada em negrito)
#A saída deve estar formatada exatamente como indicado (a string "Total: R$" 
# e o preço com um separador de milhar e duas casas decimais).
# Entrada
# Digite o nome do produto 1:calça
# Digite o preço unitário do produto 1:199.90
# Digite a quantidade do produto 1: 3
# Digite o nome do produto 2:camisa
# Digite o preço unitário do produto 2:49.95
# Digite a quantidade do produto 2:10
# Digite o nome do produto 3:cinto
# Digite o preço unitário do produto 3:25
# Digite a quantidade do produto 3:3 
# Saída:
# Total: R$1,174.20

prod_1=str(input("Digite o nome do produto 1: "))
preco_prod_1=float(input("Digite o preço unitário do produto 1:"))
quant_Vend_prod_1=int(input("Digite a quantidade do produto 1:"))
Valor_tt_prod_1=preco_prod_1*quant_Vend_prod_1

prod_2=str(input("Digite o nome do produto 2: "))
preco_prod_2=float(input("Digite o preço unitário do produto 2:"))
quant_Vend_prod_2=int(input("Digite a quantidade do produto 2:"))
Valor_tt_prod_2=preco_prod_2*quant_Vend_prod_2

prod_3=str(input("Digite o nome do produto 3: "))
preco_prod_3=float(input("Digite o preço unitário do produto 3:"))
quant_Vend_prod_3=int(input("Digite a quantidade do produto 3:"))
Valor_tt_prod_3=preco_prod_3*quant_Vend_prod_3

total_compra=Valor_tt_prod_1+Valor_tt_prod_2 + Valor_tt_prod_3
print(f"você comprou {quant_Vend_prod_1} {prod_1}, {quant_Vend_prod_2} {prod_2} e {quant_Vend_prod_3} {prod_3}. O total da sua compra é R${total_compra:,.2f}") 