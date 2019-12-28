largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

area = altura * largura
tinta = area / 2

print('A parede tem {}m de largura e {}m de altura. Sua área mede {:.2f}m²'.format(largura, altura, area))
print('Como cada litro de tinta pinta uma área de 2m², então precisamos de {:.2f}L de tinta'.format(tinta))