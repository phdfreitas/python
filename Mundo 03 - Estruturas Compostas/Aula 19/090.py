#
# Created by Pedro Freitas on 15/01/2020.
#

aluno = {}

nome = str(input('Digite o nome do aluno: '))
media = float(input('Digite a média do aluno: '))

aluno['Nome'] = nome
aluno['Media'] = media

if media >= 7:
	aluno['Situacao'] = 'Aprovado' 
else:
	aluno['Situacao'] = 'Reprovado'

for k, v in aluno.items():
	print(f'{k} é igual a {v}')