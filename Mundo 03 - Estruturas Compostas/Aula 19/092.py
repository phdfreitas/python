#
# Created by Pedro Freitas on 16/01/2020.
#

from datetime import date

dados = {}

nome = str(input('Digite o nome: '))
ano = int(input('Digite o ano de nascimento: '))
ctps = int(input('Digite a CTPS: '))

idade = date.today().year - ano

dados['Nome'] = nome
dados['Idade'] = idade
dados['CTPS'] = ctps

if ctps != 0:
	contrato = int(input('Ano de contratação: '))
	salario = float(input('Digite o salário: '))

	dados['Ínicio do Contrato'] = contrato
	dados['Salário'] = salario
	dados['Aposentadoria'] = (idade - (date.today().year - contrato)) + 35

for k, v in dados.items():
	print(f'{k:<20} ===> {v}')