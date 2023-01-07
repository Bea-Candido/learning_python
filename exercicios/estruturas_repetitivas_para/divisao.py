n= int; numerador= int; denominador= int; divisao=float;

n= int(input("Quantos casos você vai digitar?"))

for i in range(n):
       numerador = int(input("Entre com o numerador:"))
       denominador= int(input("Entre com o denominador:"))

       if denominador == 0:
            print("Divisao Impossível")
       else:
           divisao= float(numerador) / denominador 
           print(f"Divisao = {divisao}")     
           