#
# Created by Pedro Freitas on 14/01/2020.
#

total = mil = barato = 0
nomeBarato = ' '

while True:
	produto = str(input('\033[1;37mDigite o nome do produto: ')).title()
	preco = float(input('Digite o preço do produto: '))

	if total == 0:
		barato = preco
		nomeBarato = produto
	else:
		if preco < barato:
			barato = preco
			nomeBarato = produto

	total += preco

	if preco > 1000:
		mil += 1

	resposta = ' '
	while resposta not in 'SN':
		resposta = str(input('\nVocê deseja continuar? [S/N]\nSua resposta: ')).upper()

	if resposta != 'S':
		print(f'\nO total gasto em produtos foi de R$ {total:.2f} reais.')
		print(f'{mil} produtos custam mais de R$ 1000.00 reais.')
		print(f'O produto mais barato é {nomeBarato} e ele custa R$ {barato:.2f} reais.')
		break