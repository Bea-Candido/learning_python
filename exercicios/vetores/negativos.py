n= int;

n= int(input("Quantos numeros você vai digitar?"))

vetor=[0 for x in range(n)]

for i in range(n):
       vetor[i]= int(input("Digite um numero:"))

print("NUMEROS NEGATIVOS")

for i in range(n):
         if vetor[i] < 0:
             print(vetor[i])