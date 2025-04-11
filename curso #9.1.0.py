numero = int(input("informe um numero: "))

print("analisando seu numero. . . .")


u = numero // 1
d = numero // 10
c = numero // 100
m = numero // 1000

print("O numero {}".format(numero))

print("Unidade: {}".format(d))

print("Centena: {}".format(c))

print("Milhar: {}".format(m))
