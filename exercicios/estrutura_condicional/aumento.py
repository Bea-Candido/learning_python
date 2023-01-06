salario = float; novoSalario= float; aumento= float; porcentagem= int;

salario= float(input("Digite o salário da pessoa:"))

if salario <= 1000.0:
        porcentagem = 20
        aumento = salario * porcentagem / 100
        novoSalario = salario + aumento 
elif salario <= 3000.00:
        porcentagem = 15
        aumento = salario * porcentagem / 100
        novoSalario = salario + aumento 
elif salario <= 8000.0:
       porcentagem = 10
       aumento = salario * porcentagem / 100
       novoSalario = salario + aumento 
else: 
       porcentagem = 5
       aumento = salario * porcentagem / 100
       novoSalario = salario + aumento   


print(f"Novo salario = R${novoSalario}")
print(f"Aumento = {aumento}")
print(f"Porcentagem= {porcentagem}%")