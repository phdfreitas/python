#
# Created by Pedro Freitas on 14/01/2020.
#

cinquenta = vinte = dez = um = 0

saque = int(input('\033[1;37mQual o valor você deseja sacar? R$ '))

cinquenta = saque // 50
vinte = (saque % 50) // 20
dez = ((saque % 50) % 20) // 10
um = (((saque % 50) % 20) % 10)

if cinquenta != 0:
	print(f'Total de {cinquenta} cédulas de R$50.00')
if vinte != 0:
	print(f'Total de {vinte} cédulas de R$20.00')
if dez != 0:
	print(f'Total de {dez} cédulas de R$10.00')
if um != 0:
	print(f'Total de {um} cédulas de R$1.00')