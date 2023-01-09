n: int
media: float

n = int(input("Quantos alunos serao digitados? "))

nomes  = [0 for x in range(n)]
notas1 = [0 for x in range(n)]
notas2  = [0 for x in range(n)]

for i in range(n):
	print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno:")
	nomes[i] = str(input())
	notas1[i] = float(input())
	notas2[i] = float(input())

print("Alunos aprovados:")

for i in range(n):
	media = (notas1[i] + notas2[i]) / 2

	if media >= 6.0:
		print(nomes[i])