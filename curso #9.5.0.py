nome = str(input("Digite seu nome: ")).strip()#tem q usar esse strip para retirar os espaços


n = nome.split() # separa a string em uma lista de strings

print("Olá , {}!".format(nome)) #imprime a string com o nome do usuário

print("Seu Primeiro Nome é: {}".format(n[0]))


print("Seu ultimo nome é : {}".format(n[-1])) #imprime o último nome do usuário