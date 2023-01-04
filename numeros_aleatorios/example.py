import random

lista= [3,13,7]
numero = random.choice(lista)
print(numero)


numero = random.randint(0,10)
print(numero)

random.seed(1)
numero = random.randint(0,10)
print(numero)