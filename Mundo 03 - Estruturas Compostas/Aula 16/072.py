#
# Created by Pedro Freitas on 14/01/2020.
#

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
		   'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
		   'Dezeoito', 'Dezenove', 'Vinte')

numero = int(input('\033[1;37mDigite um número entre 0 e 20: '))

while numero < 0 or numero > 20:
	numero = int(input('\033[1;37mTente novamente. Digite um número entre 0 e 20: '))	

for n, ext in enumerate(numeros):
	if numero == n:
		print(f'O número {numero} se escreve da seguinte forma: {ext}')