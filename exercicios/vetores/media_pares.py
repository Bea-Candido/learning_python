n: int; somapares: int; npares: int
mediapares: float

n = int(input("Quantos elementos vai ter o vetor? "))

vetor = [0 for x in range(n)]

for i in range(n):
	vetor[i] = int(input("Digite um numero: "))

npares = 0
somapares = 0
for i in range(n):
	if vetor[i] % 2 == 0:
		somapares = somapares + vetor[i]
		npares = npares + 1

if npares == 0:
	print("Nenhum numero par")
else:
	mediapares = float(somapares) / npares

	print(f"Media dos pares = {mediapares}")