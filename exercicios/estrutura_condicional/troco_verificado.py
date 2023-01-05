preco = float; qtd= int; 
dinheiro = float; troco= float;
faltam= float; 

preco = float(input("Preço unitário do produto:"))
qtd = int(input("Quantidade comprada:"))
dinheiro= float(input("Dinheiro recebido:"))

if preco * qtd > dinheiro :
        faltam = preco *qtd - dinheiro
        print(f"DINHEIRO INSUFICIENTE,FALTAM :{faltam} REAIS")
else:
        troco = dinheiro - preco *qtd
        print(f"TROCO{troco}")        


