vendas_tecnologias={"Iphone":15000,"Samsung Galaxy":12000,"Tv samsung":10000,"PS5":10000,"Tablet":1720,"Ipad":1200}

#demostrando o for
for chave in vendas_tecnologias:
    print("O produto {} vendeu {} unidades".format(chave,vendas_tecnologias[chave]))

print()

for item in vendas_tecnologias.items():
    print(item)

print()

for produto,vendas in vendas_tecnologias.items():
    print("{}: {} de unidades".format(produto,vendas))