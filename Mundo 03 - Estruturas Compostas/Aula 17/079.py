#
# Created by Pedro Freitas on 14/01/2020.
#

lista = []

while True:
	numero = int(input('\033[1;37mDigite um número inteiro. *Lembre-se que valores repetidos não serão adicionados*.\nAdicionar o número: '))
	
	if (numero in lista) == False:
		lista.append(numero)   

	resposta = str(input('Continuar adicionando? [S/N] ')).upper()
	
	while resposta not in 'SN':
		resposta = str(input('Você digitou algo errado. Continuar adicionando? [S/N] ')).upper()

	if resposta != 'S':
		break
lista.sort()
print(f'Os valores digitados em ordem crescente são {lista}')