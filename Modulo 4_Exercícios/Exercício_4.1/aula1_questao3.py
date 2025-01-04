n1 = int (input (f"Digite os valores: "))
n2 = int (input (f"Digite os valores: "))
n3 = int (input (f"Digite os valores: "))

med=(n1+n2+n3)/3

if med>=60:
    print(f"Aprovado")
    print(f"FIM")
elif med<60 and med>=40:
    print(f"Recuperação")
    print(f"FIM")
else:   
    print(f"Reprovado")
    print(f"FIM")