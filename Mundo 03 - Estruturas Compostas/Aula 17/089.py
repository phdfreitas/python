#
# Created by Pedro Freitas on 15/01/2020.
#

dados = []
alunos = []

while True:
	dados.append(str(input('\033[1;37mNome do Aluno: ')))
	dados.append(float(input('Nota 1: ')))
	dados.append(float(input('Nota 2: ')))

	alunos.append(dados[:]) 
	dados.clear()

	''' Outra maneira de fazer seria separar os "dados" e colocar os mesmos
		dentro de uma lista e fazer o append na lista principal, ou seja:
		*alunos.append([nome, [nota1, nota2], media])*
	'''
	
	resposta = str(input('Você deseja continuar? [S/N] ')).upper()
	while resposta not in 'SN':
		resposta = srt(input('Algo deu errado. Você deseja continuar? [S/N] ')).upper()

	if resposta != 'S':
		break

print('_'*50)
print(f'{"ID":<16}{"Nome do Aluno":<24}{"Média Final"}')
print('_'*50)

for ident, boletim  in enumerate(alunos):
	print(f'{ident + 1:<16} {boletim[0]:<22} {((boletim[1] + boletim[2]) / 2):.2f}')

sn = str(input('Você deseja continuar e ver as notas dos alunos? [S/N] ')).upper()
while sn not in 'SN':
	sn = srt(input('Algo deu errado. Você deseja continuar? [S/N] ')).upper()

	if sn != 'S':
		break
if sn == 'S':
	print('Para encerrar o programa digite -1.')
	idAluno = int(input('Digite o ID do aluno que deseja ver as notas: '))
	while idAluno != -1:
		print(f'As notas de {alunos[idAluno - 1][0]} foram: {alunos[idAluno - 1][1]} e {alunos[idAluno - 1][2]}')
		idAluno = int(input('Digite o ID do aluno que deseja ver as notas: '))