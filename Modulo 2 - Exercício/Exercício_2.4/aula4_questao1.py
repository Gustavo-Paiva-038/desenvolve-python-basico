#Faça um programa para ler as dimensões de um terreno em inteiros 
# (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. 
# Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:
# O terreno possui 250m2 e custa R$512,490.50
# Comente na linha acima de cada instrução uma breve descrição da instrução.
# Fórmulas:
# area_m2 = comprimento * largura
# preco_total = preco_m2 * area_m2

#Entrada de dados: aqui o usuário irá inserir o comprimento, largura e valor por m2 do terreno,
comprimento=int(input("Infomorme o comprimento do terreno: "))
largura=int(input("Infomorme a largura do terreno: "))
preco_m2=(float(input("Infomorme o valor por m2 do terreno: ")))

#Procesamento dos dados: será calculado a area e o valor a ser pago por m2 da area.
area_m2= comprimento * largura 
valor_do_terreno=preco_m2*area_m2

#Saída de dados: será informado a area total do terreno e o valor de venda.
print (f"O terreno possui {area_m2:,.2f}m2 e custa R$ {valor_do_terreno:,.2f}")