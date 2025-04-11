nome = str(input("Digite o seu nome completo: ")).strip()
print("Analisando seu nome...")

print("Seu nome em maiusculo é : {}".format(nome.upper()))

print("Seu nome em minusculo é : {}".format(nome.lower()))

print("Total de caracteres é : {}".format(len(nome)- nome.count(" ")))

print("Seu Primeiro nome tem ao todo {} letras".format(nome.find(" ")))

separar= nome.split()

print("Seu primeiro nome é {} e tem {} letra".format(separar[0], len(separar[0])))