n= int; valor= int;

n = int(input("Quantos numeros você vai digitar?"))

for i in range (n):
       valor= int(input("Digite um numero:"))

       if valor == 0:
                print("Nulo")
       else:
                if valor % 2 ==  0:   
                    print("Par")
                else:
                    print("Impar")
                if valor > 0:
                    print("POSITIVO")
                else:
                    print("NEGATIVO")            
