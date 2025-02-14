produtos=["apple", "tv","mac", "iphone x", "IPad", "apple watch", "mac book", "airpods"]
novos_produtos=["Chromecast","windows phone"]
produtos.extend(novos_produtos)
print(produtos)

#Usando concatenação

print("Usando o '+'")
produtos_compilados=produtos+novos_produtos
print(produtos_compilados)

#Usando o append

print("Usando append")
produtos.append(novos_produtos)
print(produtos)