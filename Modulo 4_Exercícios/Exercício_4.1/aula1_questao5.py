#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes.
#Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente.
#Ao final, imprima a média das idades.
# (idade1 + idade2 + idade3 + … + idade_n)/N

n_respond=int(input(f"digite o número de respondentes: "))

soma=0
cont=0

while cont<n_respond:
    idade=int(input(f"Digite as idades: "))
    soma +=idade
    cont +=1

print(f"A média da idades é: {soma/n_respond:.0f} anos")