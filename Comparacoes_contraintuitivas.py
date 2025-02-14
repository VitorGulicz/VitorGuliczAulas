faturamento=input("Qual foi o faturamento da loja nesse mes? ")
custo=input("Qual foi o custo da loja nesse mes? ")
if faturamento!="" and custo!="":
    lucro= int(faturamento)-int(custo)
    print("O lucro da loja foi de {} R$".format(lucro))
else:
    print("Algum valor não foi fornecido")

#Outro metodo:

    faturamento=input("Qual foi o faturamento da loja nesse mes? ")
custo=input("Qual foi o custo da loja nesse mes? ")
if faturamento and custo:
    lucro= int(faturamento)-int(custo)
    print("O lucro da loja foi de {} R$".format(lucro))
else:
    print("Algum valor não foi fornecido")