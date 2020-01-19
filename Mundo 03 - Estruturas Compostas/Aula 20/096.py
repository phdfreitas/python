#
# Created by Pedro Freitas on 18/01/2020.
#

def area(largura, comprimento):
	print(f'A área do terreno de {largura:.2f} x {comprimento:.2f} é de {(largura * comprimento):.1f}m²')

lar = float(input('Largura (m): '))
com = float(input('Comprimento (m): '))

area(lar, com)