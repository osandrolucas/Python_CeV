#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

print('#' * 20)
largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
area =  altura * largura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{}, sua área é {}m² e você precisará de {}l de tinta para pintar a parede!'.format(largura,altura,area,tinta))
