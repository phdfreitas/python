#
# Created by Pedro Freitas on 09/01/2020.
#

valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quanto você ganha por mês? R$ '))
anos = int(input('Em quantos anos você pretende pagar? ')) * 12

parcela = valor / anos

if parcela <= (salario * 0.3):
	print('Parabéns! Você poderá comprar a casa.')
else:
	print('Infelizmente o valor da parcela é maior que "30%" do seu salário e por isso o empréstimo foi negado.')