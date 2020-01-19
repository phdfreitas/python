#
# Created by Pedro Freitas on 16/01/2020.
#

dados = {}
infos = []
media = 0

while True:
	dados['nome'] = str(input('Nome: '))
	dados['sexo'] = str(input('Sexo [M/F]: '))
	dados['idade'] = int(input('Idade: '))

	media += dados['idade'] 

	infos.append(dados.copy())
	dados.clear()

	resposta = str(input('Deseja continuar? [S/N] ')).upper()

	if resposta == 'N':
		break

print(f'- {len(infos)} pessoas foram cadastradas.')
print(f'- A média de idade do grupo é de {media / len(infos)} anos.')
print('- As mulheres cadastradas foram: ', end='')
for k, v in enumerate(infos):
	if(v['sexo'] == 'F'):
		print(f'{v["nome"]} ', end='')
print()
print('- Abaixo temos as pessoas com idade acima da média: ')
for k, v in enumerate(infos):
	if(v['idade'] > media / len(infos)):
		print(f'Nome: {v["nome"]}, Idade: {v["idade"]}, Sexo: {v["sexo"]}')