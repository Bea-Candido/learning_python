# Dados da primeira pessoa:
# Nome: Maria Silva
# Idade: 19
# Dados da segunda pessoa:
# Nome: Joao Melo
# Idade 20
# A idade média de Maria Silva e Joao Melo é de 19.5 anos

nome1 = str; 
idade1= int;
nome2= str; 
idade2= int;
media = float;

print("Dados da primeira pessoa:")
nome1= str(input("Nome?"))
idade1= int(input("Idade?"))
print("Dados da segunda pessoa")
nome2= str(input("Nome?"))
idade2= int(input("Idade?"))

media= (idade1 + idade2) / 2 

print(f"A idade média de,{nome1} e {nome2} é de {media}")