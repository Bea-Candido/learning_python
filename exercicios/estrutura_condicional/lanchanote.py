codigo = int; qtd= int;
valor = float;

codigo= int(input("Codigo do produo comprado:"))
qtd= int(input("Quantidade comprada:")) 

valor = 0
if codigo == 1:
    valor = qtd *5.0
elif codigo == 2:
    valor = qtd * 3.50
elif codigo == 3:
    valor = qtd * 4.80
elif codigo == 4:
    valor = qtd * 8.90
elif codigo == 5:
    valor = qtd *7.32

print(f"Valor a pagar: R${valor}")                