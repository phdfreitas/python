#
# Created by Pedro Freitas on 14/01/2020.
#

tupla = ('Pedro', 'Ana', 'Carlos', 'Maria', 'Jose', 'Lobo', 'Cachorro',
		 'Futebol', 'Bolo', 'Caderno', 'Criança', 'Jovem', 'Adulto', 'Dinheiro')

for pos, palavra in enumerate(tupla):
	tam = len(palavra)
	print(f'\033[1;37mAs vogais de {palavra.upper()} são:')
	
	for x in range(0, tam):
		if (palavra.lower()[x] == 'a' or palavra.lower()[x] == 'e' or
		    palavra.lower()[x] == 'i' or palavra.lower()[x] == 'o' or 
		    palavra.lower()[x] == 'u'):

			print(f'\033[1;31m{palavra.upper()[x]}', end=' ')
	print()