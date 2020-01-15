#
# Created by Pedro Freitas on 15/01/2020.
#

dados = []
db = []

while True:
	dados.append(str(input('\033[1;37mNome: ')))
	dados.append(float(input('Peso: ')))

	db.append(dados[:]) #faço a copia dos dois valores (lista) para uma nova lista (lista de listas)
	dados.clear()
	
	resposta = str(input('Você deseja continuar? [S/N] ')).upper()
	while resposta not in 'SN':
		resposta = srt(input('Algo deu errado. Você deseja continuar? [S/N] ')).upper()

	if resposta != 'S':
		break

print(f'Um total de {len(db)} pessoas foram cadastradas.')

print('Considerando que as pessoas mais leves têm menos de 65Kg, entre os cadastrados temos: ')
for pessoa in db:
	if (pessoa[1] < 65):
		print(f'{pessoa[0]}')
print('Considerando que as pessoas mais pesadas têm mais de 100Kg, entre os cadastrados temos: ')
for pessoa in db:
	if (pessoa[1] > 100):
		print(f'{pessoa[0]}')