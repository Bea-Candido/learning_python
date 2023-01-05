nome = str;
valorHora = float;
horasTrabalhada = int;
salario = float;

nome= str(input("Nome:"))
valorHora= float(input("Valor por hora:"))
horastrabalhada = int(input("Horas trabalhadas:"))

salario = valorHora * horastrabalhada 

print(f"O pagamento para {nome} deve ser de {salario}")
