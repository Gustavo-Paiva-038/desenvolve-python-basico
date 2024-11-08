#3 - 
#Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. 
# Escreva um programa em Python que pergunte ao usuário sua idade, 
# se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False)
# quantas vezes venceu um jogo. 

# A- O programa deve imprimir True se o participante tiver entre 16 e 18 anos, 
# B- já tiver jogado pelo menos 3 jogos
# C- já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. 

# Sua expressão deve imprimir False caso contrário. 
# Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em laranja 
# e as impressões de seu código em branco.

#Terminal
# Digite sua idade: 17
# Já jogou pelo menos 3 jogos de tabuleiro? True
# Quantos jogos já venceu? 2
# Apto para ingressar no clube de jogos de tabuleiro: True20

idade=int(input(f"Digite sua idade: "))
num_jogos=int(input(f"Quantos jogos de tabuleiro já jogou? "))
jogos_venc=int(input(f"Quantos jogos venceu? "))

a= idade>15 and idade<19
b=num_jogos>=3
c=jogos_venc>=1

apto=a and b and c

print(f"Sua idade: ", idade)
print(f"Já jogou pelo menos 3 jogos de tabuleiro? ", b)
print(f"Quantos jogos já venceu? ", jogos_venc)
print (f"Apto para ingressar no clube de jogos de tabuleiro:", apto)