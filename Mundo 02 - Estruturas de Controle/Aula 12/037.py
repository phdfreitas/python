#
# Created by Pedro Freitas on 09/01/2020.
#

num = int(input('\033[1;33mDigite um número qualquer: '))

print('Para qual base númerica você deseja converter {} ?\nDigite: ')

res = str(input('1 Para binário\n2 Para Octal\n3 Para Hexadecimal\nSua resposta: '))

if res == '1':
	print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif res == '2':
	print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
else:
	print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))