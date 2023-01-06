idade= int; soma = float; qtd= int;
media= float;

print("Digite as idades:")
idade = int(input())

if idade < 0:
        print("Impossível calcular")
else:
       soma = 0
       qtd = 0     
while idade >= 0:
   soma = soma+ idade
   qtd = qtd + 1
   idade = int(input())

media = soma / qtd

print(f"MEDIA= {media}")
