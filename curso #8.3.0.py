import random

#Coleta o nomes dos aluno
aluno_1 = input("Qual é o nome dos aluno 1: ")
aluno_2 = input("Qual é o nome dos aluno 2: ")
aluno_3 = input("Qual é o nome dos aluno 3: ")
aluno_4 = input("Qual é o nome dos aluno 4: ")

#faz uma lista
aluno = [aluno_1,aluno_2,aluno_3,aluno_4]

#embaralha os nomes
random.shuffle(aluno)


ap1 = "Primeiro a apresentar"
ap2 = "Segundo a apresentar"
ap3 = "Terceiro a apresentar"
ap4 = "Quarto a apresentar"

apresentações = [ap1,ap2,ap3,ap4]


for i in range(len(aluno)):
    print("O aluno {} irá ser o {}".format(aluno[i], apresentações[i]))