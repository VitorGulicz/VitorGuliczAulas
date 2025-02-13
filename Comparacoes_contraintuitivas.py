faturamento=input("Qual foi o faturamento da loja nesse mes? ")
custo=input("Qual foi o custo da loja nesse mes? ")
if faturamento<0 or custo<0:
    print("Numero Invalido")
else:
    lucro= int(faturamento)-int(custo)
print("O lucro da loja foi de {} R$".format(lucro))