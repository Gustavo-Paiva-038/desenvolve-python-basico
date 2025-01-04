#Fluxograma com loop infinito, sinais de < e > invertidos no fluxo, fiz a inverção e o codigo ficou correto.

n=int (input(f"digite um número: "))
cont=0

while n>cont:
    cont +=1
    print(cont)

n<cont
print (f"FIM")