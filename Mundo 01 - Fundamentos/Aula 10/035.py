#
# Created by Pedro Freitas on 08/01/2020.
#

a = float(input('Digite um valor para primeira reta: '))
b = float(input('Digite um valor para segunda reta: '))
c = float(input('Digite um valor para terceira reta: '))

if ((a < b + c) and (a > abs(b - c))) and ((b < a + c) and (b > abs(a - c))) and ((c < a + b) and (c > abs(a - b))):
	print('Sim, é possível construir um triângulo com os valores de a, b e c.')
else:
	print('Infelizmente com os valores de a, b e c não é possível construir um triângulo.')  