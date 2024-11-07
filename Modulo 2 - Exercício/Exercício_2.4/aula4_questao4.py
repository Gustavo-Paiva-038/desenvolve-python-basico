#Escreva um programa que leia um valor inteiro referente a uma quantia em reais e 
# calcule a menor quantidade possível de notas necessárias para pagar aquele valor. 
# As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. 
# A saída deve estar formatada exatamente como indicado.
# Entrada 576
# Saída
# 5 nota(s) de R$100,00
# 1 nota(s) de R$50,00
# 1 nota(s) de R$20,00
# 0 nota(s) de R$10,00
# 1 nota(s) de R$5,00
# 0 nota(s) de R$2,00
# 1 nota(s) de R$1,00

#entradas de dados
valor_cobrado=int(input(f"Digite o valor da compra: "))
#processamento de dados
notas_100=int(valor_cobrado//100)
notas_50=int ((valor_cobrado-(notas_100*100))//50)
notas_20=int((valor_cobrado-(notas_100*100)-(notas_50*50))//20)
notas_10=int((valor_cobrado-(notas_100*100)-(notas_50*50)-(notas_20*20))//10)
notas_5=int((valor_cobrado-(notas_100*100)-(notas_50*50)-(notas_20*20)-(notas_10*10))//5)
notas_2=int((valor_cobrado-(notas_100*100)-(notas_50*50)-(notas_20*20)-(notas_10*10)-(notas_5*5))//2)
notas_1=int((valor_cobrado-(notas_100*100)-(notas_50*50)-(notas_20*20)-(notas_10*10)-(notas_5*5)-(notas_2*2))//1)

print(f"Serão necessárias: ")
print(f"{notas_100} nota(s) de R$100,00")
print(f"{notas_50} nota(s) de R$50,00")
print(f"{notas_20} nota(s) de R$20,00")
print(f"{notas_10} nota(s) de R$10,00")
print(f"{notas_5} nota(s) de R$5,00")
print(f"{notas_2} nota(s) de R$2,00")
print(f"e {notas_1} nota(s) de R$1,00")
