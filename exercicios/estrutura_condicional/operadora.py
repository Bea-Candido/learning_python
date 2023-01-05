minutos= int; minutosExtra = int;
valor = int;

minutos= int(input("Digite a quantidade de minutos:"))

minutosExtra = (minutos - 100)*2
valor= minutosExtra + 50 

if minutos <= 100 : 
   print(f"Valor a pagar:50")
else:
    print(f"Valor a pagar:{valor}")   
