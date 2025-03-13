Dias = int(input("Quantos Dias o carro foi alugado ? "))

Kms = float(input(" Quantos Km o carro foi rodado ? "))

Custo_diaria = Dias * 60 
Custo_Km = Kms * 0.15

print("Você rodou {}Km e alugou o carro por {} dias".format(Kms,Dias))

Valor_total = Custo_diaria + Custo_Km

print("Valor total a pagar é de R${:.2f}".format(Valor_total))


