import random


aluno_1 = input("Qual é o nome dos aluno 1: ")
aluno_2 = input("Qual é o nome dos aluno 2: ")
aluno_3 = input("Qual é o nome dos aluno 3: ")
aluno_4 = input("Qual é o nome dos aluno 4: ")


aluno = [aluno_1,aluno_2,aluno_3,aluno_4]

aluno_sorteado = random.choice(aluno)


print (" O aluno sorteado para apagar o quadro é:  ", aluno_sorteado)