produtos1=["tv", "celular", "mouse", "teclado", "tablet"]
vendas=[1000, 1500, 350, 270 , 900]
print("As vendas de ",produtos1[1],"foram de",vendas[1])

i=produtos1.index("mouse")
print("O produto da posição i é "+ str(produtos1[i])) 


produtos=["tv", "celular", "mouse", "teclado", "tablet","geladeira","forno"]
estoque=[100,150,100,120,70,180,80]
produto=input("Insira o nome do produto em letra minuscula: ")
if produto in produtos:
    i=produtos.index(produto)
    qtde_estoque=estoque[i]
    print("Possuimos {} unidades de {} no estoque".format(qtde_estoque,produto))
else:
    print("Não possuimos {} no estoque".format(produto)) 