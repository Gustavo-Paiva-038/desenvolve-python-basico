#2
#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. 
# Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme 
# em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:
# Se a avaliação for 5, imprima "Excelente!"
# Se a avaliação for 4, imprima "Muito Bom!"
# Se a avaliação for 3, imprima "Bom!"
# Se a avaliação for 2, imprima "Regular."
# Se a avaliação for 1, imprima "Ruim."

aval=int(input(f"Avalie o filme de 1 à 5 conforme sua percepção, onde 0 é Ruim e 5 é Execelente: "))
if aval==5:
    print ("Excelente")
else:
    if aval==4:
        print("Muito Bom")
    else:
        if aval==3:
            print("Bom")
        else:
            if aval==2:
                print("Regular")
            else:
                if aval==1:
                    print("Ruim")
                else:
                    print ("Avaliação invalida.")



#print(f"Excelente" if aval==5 else "Muito Bom" if aval==4 else)
#print ()
#print (f"Bom" if aval==3:)