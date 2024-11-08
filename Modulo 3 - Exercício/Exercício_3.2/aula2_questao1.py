# 1 - 
# Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17).
# Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos,
# indicando que podem entrar no bar, e False caso contrário.

idad_ju=int(input(f"Informe a idade de Juliana: "))
idad_cris = int(input(f"Informe a idade de Cris: "))

print (idad_ju>17 and idad_cris>17)