width = float(input("Qual a largura da parede em Metros: "))

height= float(input("E a altura da parede em Metros: "))

area = width * height

Tinta = area / 2

print ("Para pintar {:.1f}m x {:.1f}m de parede você precisa de {}L de tinta".format(width,height,Tinta))