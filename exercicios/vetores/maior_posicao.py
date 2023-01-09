n: int; qtdpares: int

n = int(input("Quantos numeros voce vai digitar? "))

vetor =  [0 for x in range(n)]

for i in range(n):
	vetor[i] = int(input("Digite um numero: "))

print("Numeros pares:")

qtdpares = 0
for i in range(n):
	if vetor[i] % 2 == 0:
		print(f"{vetor[i]}  ", end="")
		qtdpares = qtdpares + 1

print(f"Quantidade de pares= {qtdpares}")