#Exercício de maratona:  https://www.beecrowd.com.br/judge/pt/problems/view/1094
#Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. 
#Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. 
#Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 

#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. 
#As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C')
#com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).

#Saída: Apresente o total de cobaias utilizadas, 
#o total de cada tipo de cobaia e 
#o percentual de cada uma em relação ao total de cobaias utilizadas

q_exper=int(input(f"Número de experiencias realizadas: "))

cont=0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

while cont<q_exper:
    quant=int(input( ))
    tipo=input()
    if tipo== 'S':
        soma_sapo +=quant
    elif tipo== 'C':
        soma_coelho += quant
    elif tipo == 'R':
        soma_rato +=quant

    cont +=1
    tt_cobaias = soma_rato+soma_sapo+soma_coelho
print(f"Total de cobaias utilizadas: {tt_cobaias}")
print(f"Total de ratos: {soma_rato}, que representa {soma_rato/tt_cobaias*100:.2f}% das cobaias utilizadas")
print(f"Total de coelhos: {soma_coelho}, que representa {soma_coelho/tt_cobaias*100:.2f}% das cobaias utilizadas")
print(f"Total de sapos: {soma_sapo}, que representa {soma_sapo/tt_cobaias*100:.2f}% das cobaias utilizadas")