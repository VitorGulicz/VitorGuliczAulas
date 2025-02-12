#Faça um programa que receba uma nota do aluno e se for superior ou igual a 7 apareça mensagem que ele está aprovado, se for inferior a 5 ele esta "Não aprovado/reprovado direto
#e se estiver entre 5 e 7 apareça mensagem "Não aprovado/Recuperação"
num=int(input("Digite a nota do aluno: "))
if num>=7:
    print("Aluno aprovado")
else:
    if num<5:
        print("Aluno reprovado")
    else:
        print("Aluno em recuperação")