Estoque=[1200,300,800,1500,1900,2750,400,20,23,70,90,80,1100]
produtos=["Coca cola","Pepsi","Guarana","Skol","Brahma","Agua","Del vale","Red bull","Dolly","Fanta","Sprite","Sukita","Pepsi Twist"]
nivel_minimo=50
for i,qtde in enumerate(Estoque):
    if qtde < nivel_minimo:
        print(produtos[i],qtde)