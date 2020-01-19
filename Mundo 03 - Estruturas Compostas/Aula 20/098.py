#
# Created by Pedro Freitas on 18/01/2020.
#

def contador(inicio, fim, passo):

	if passo == 0:
		print(f'Contagem de {inicio} até {fim} de {1} em {1}: ', end = '')
		if inicio <= fim:
			for c in range(inicio, fim + 1, 1):
				print(f'{c} ', end = '')
			print()
		elif inicio > fim:
			for c in range(inicio, fim - 1, -1):
				print(f'{c} ', end = '')
			print()	
	else:	
		print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}: ', end = '')
		if inicio <= fim:
			for c in range(inicio, fim + 1, passo):
				print(f'{c} ', end = '')
			print()
		elif inicio > fim or passo < 0:
			for c in range(inicio, fim - 1, abs(passo) * -1):
				print(f'{c} ', end = '')
			print()	

contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Faça uma contagem personalizada:\nInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)