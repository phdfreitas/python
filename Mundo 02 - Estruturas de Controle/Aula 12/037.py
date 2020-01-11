#
# Created by Pedro Freitas on 09/01/2020.
#

num = int(input('Digite um número qualquer: '))

print('Para qual base númerica você deseja converter {} ?\nDigite: ')

res = str(input('1 Para binário\n2 Para Octal\n3 Para Hexadecimal\nSua resposta: '))

if res == 1:
	print(dec2any(num, 2))
elif res == 2:
	print(oct(num))
else:
	print(hex(num))
 