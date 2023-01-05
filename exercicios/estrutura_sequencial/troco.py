# Preço unitário do produto: 8.00
# Quantidade comprada: 2
# Dinheiro recebido: 20.00
# TROCO = 4.00

unitario = int;
quantidade = int;
dinheiroRecebido = float;
troco = float;
total = float;

unitario = int(input("Preço unitário do produto:"))
quantidade = int(input("Quantidade comprada:"))
dinheiroRecebido = float(input("Dinheiro recebido:"))

total = (unitario * quantidade ) 

troco = dinheiroRecebido - total


print(f"Troco:{troco}")