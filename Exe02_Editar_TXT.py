arquivo2=open("C:/Users/vitor_gulicz/Documents/Txt/GOT.txt","w")
arquivo2.write("Escrevendo no arquivo\n")
arquivo2.write("John Snow\n")
arquivo2.write("Arya Stark\n")
arquivo2.write("Sansa Stark\n")
arquivo2.write("Bran Stark\n")
arquivo2.close()
print("Fim do programa")

with open("C:/Users/vitor_gulicz/Documents/Txt/Resumo 3.txt","w")as arquivo3:
    arquivo3.write("Escrevendo arquivo\n")
    arquivo3.write("Capitão Stoltomayer\n")
print("Fim programa")