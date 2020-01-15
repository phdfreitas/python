#
# Created by Pedro Freitas on 14/01/2020.
#

lista = []

while True:
	lista.append(int(input('\033[1;37mDigite um número: ')))

	resposta = str(input('Você deseja continuar? [S/N] ')).upper()
	while resposta not in 'SN':
		resposta = str(input('Algo deu errado, tente novamente. Você deseja continuar? [S/N] ')).upper()

	if resposta != 'S':
		break
		
print(f'Um total de {len(lista)} números foram digitados.')
lista.sort(reverse = True)
print(f'A lista de números em ordem decrescente é {lista}')

if (5 in lista):
	print('Sim, o valor 5 está na lista.')
else:
	print('O valor 5 não foi encontrado na lista.')