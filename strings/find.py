minha_string = "it's a new year new opportunities to get it right.... and to make mistakes!"

busca = minha_string.find("mistakes")
print(busca)

print(minha_string[busca:])

minha_string = minha_string.replace("mistakes","error404")
print(minha_string)