meu_dicionario = {"A":"AMEIXA","B":"Bola","C":"Cachorro"}

print(meu_dicionario["A"])
print(meu_dicionario)

for chave in meu_dicionario:
    print(chave + ":" + meu_dicionario[chave])

for i in meu_dicionario.values():
    print(i)    