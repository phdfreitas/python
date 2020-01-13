#
# Created by Pedro Freitas on 13/01/2020.
#

sexo = ''
while sexo != 'M' and sexo != 'F':
	sexo = str(input('\033[1;33mDigite o sexo da forma correta [M/F]: ')).upper()
	
	if sexo != 'M' and sexo != 'F': 
		print('Você não digitou da maneira correta. Tente novamente.')
