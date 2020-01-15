#
# Created by Pedro Freitas on 14/01/2020.
#

exp = str(input('\033[1;37mDigite a expressão: '))

pares = [] #inicia a lista vazia

for c in exp: #para cada 'char' da expressão

	if c == ')' and len(pares) == 0: #se a lista (pares) ainda não possuir char do tipo '('
		print('A expressão está errada.')
		break
	elif c == '(': # quando é um char do tipo '(', adicionamos a lista
		pares.append(c)
	elif c == ')' and len(pares) > 0: # se a lista já estiver com algum elemento
		pares.pop()					  # esse elemento só pode ser '(', dessa forma,
									  # ao encontrarmos o outro ')', encontramos o PAR e
									  # podemos remover ele. 	
if len(pares) == 0:
	print('A expressão está correta.')
else:
	print('A expressão está errada.')