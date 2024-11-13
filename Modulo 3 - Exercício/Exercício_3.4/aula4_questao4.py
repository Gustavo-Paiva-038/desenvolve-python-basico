#4
#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete
#  com base na distância e no peso do pacote. 
# Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. 
# O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

dist= int(input(f"Informe a distância entre a retirada e a entrega do encomenda: "))
peso= int(input(f"Informe o peso do item a ser transportado: "))

if dist<=100 and peso <=10:
    print(f"R$", peso*1)
else:
    if dist>=101 and dist<=300 and peso <=10:
        print(f"R$", peso*1.5)
    else:
        if dist>300 and peso <=10:
            print(f"R$", peso*2)
        else:
            if dist<=100 and peso >10:
                print(f"R$", peso*1+10)
            else:
                if dist>=101 and dist<=300 and peso>10:
                    print(f"R$", peso*1.5+10)
                else:
                    if dist>300 and peso>10:
                        print(f"R$", peso*2+10)
                    else:
                        print (f"Dados invalidos")