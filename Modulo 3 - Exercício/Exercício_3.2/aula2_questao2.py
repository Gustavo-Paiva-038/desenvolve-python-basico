#2 -
# Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos 
# uma pessoa é maior de idade (ficando responsável pelas outras). 
# Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, 
# mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, 
# e False caso contrário.

idad_ju=int(input(f"Informe a idade de Juliana: "))
idad_cris = int(input(f"Informe a idade de Cris: "))

print (idad_ju>17 or idad_cris>17)