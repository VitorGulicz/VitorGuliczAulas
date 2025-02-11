#Transforma apenas a primeira letra de uma string em maiuscula
nome="vitor"
print(nome.capitalize(),"\n")

#Transforma todas as letras em minuscula
nome="VITOR"
print(nome.casefold(),"\n")

#Conta o numero de vezes que um caractere especifico aparece na string.
nome="VitorDaniel@gmail.com"
print(nome.count("i"),"\n")

#Retorna true (verdadeiro) ou false (falso) para um teste se a string termina com uma string especifica
nome="VitorDaniel@gmail.com"
print(nome.endswith("gmail.com"),"\n")

#Encontra a posição do termo procurado. Lembre-se começa do zero
nome="VitorDaniel@gmail.com"
print(nome.find("@"),"\n")

#Verifica se o texto é todo feito com letras
nome="Vitor"
print(nome.isalpha(),"\n")

#Verifica se o texto é feito com numeros
nome="123"
print(nome.isnumeric(),"\n")

#Substitui um caractere escolhido por outro
nome="Vitor"
print(nome.replace("o","u"),"\n")

#Separa o texto em string baseado em algum caractere indicado
nome="Vitor @ Daniel"
print(nome.split("@"),"\n")

#Coloca todas as letras iniciais em maiscula
nome="vitor daniel macedo gulicz"
print(nome.title(),"\n")

#Retira os caracteres indesejados, como por exemplo que não agregam valor
nome="       Vitor Daniel Macedo Gulicz"
print(nome.strip(),"\n")

#Retorna true ou false para um teste de uma string se inicia com um texto especifico
nome="vitor 2008"
print(nome.startswith("vit"),"\n")
print(nome.startswith("Vit"),"\n")