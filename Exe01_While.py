venda=input("registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ")
vendas=[]
#Crie aqui o programa
while venda !="":
    vendas.append(venda)
    venda=input("Registe um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ")
print("Registro Finalizado. As vendas cadastradas foram {}".format(vendas))