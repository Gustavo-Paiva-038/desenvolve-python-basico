n = int (input(f"Digite um numero: "))
maior=0
while n>0:
     x= int(input())
     while x>maior:
          maior=x
     n -= 1


print (maior)