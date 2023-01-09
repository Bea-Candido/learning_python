import math

n: int; indlinha: int; indcoluna: int
somapositivos: float

n = int(input("Qual a ordem da matriz? "))

matriz = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
	for j in range(n):
		matriz[i][j] = float(input(f"Elemento [{i},{j}]: "))

somapositivos = 0
for i in range(n):
	for j in range(n):
		if matriz[i][j] > 0:
			somapositivos = somapositivos + matriz[i][j]

print(f"\nSOMA DOS POSITIVOS: {somapositivos:.1f}")

indlinha = int(input("Escolha uma linha: "))

print("LINHA ESCOLHIDA: ", end="");

for i in range(n):
	print(f"{matriz[indlinha][i]:.1f} ", end="")

indlinha = int(input("\n\nEscolha uma coluna: "))

print("COLUNA ESCOLHIDA: ", end="");

for i in range(n):
	print(f"{matriz[i][indlinha]} ", end="")

print("\n\nDiagonal principal: ", end="");

for i in range(n):
	print(f"{matriz[i][i]} ", end="")

for i in range(n):
	for j in range(n):
		if matriz[i][j] < 0:
			matriz[i][j] = math.pow(matriz[i][j], 2);

print("Matriz alterada:");

for i in range(n):
	for j in range(n):
		print(f"{matriz[i][j]} ", end="")
	print()