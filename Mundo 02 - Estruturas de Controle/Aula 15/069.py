#
# Created by Pedro Freitas on 14/01/2020.
#

totalIdade = homens = mulheres = idade = sexo = 0

while True:
	idade = int(input('\033[1;37mDigite sua idade: '))
	sexo = str(input('Digite seu sexo [M/F]: '))

	if idade > 18:
		totalIdade += 1
	if sexo == 'M':
		homens += 1
	if sexo == 'F' and idade < 20:
		mulheres += 1

	resposta = str(input('\nVocê deseja continuar? [S/N]\nSua resposta: ')).upper()

	if resposta != 'S':
		print(f'\nNo total {totalIdade} pessoas têm mais de 18 anos.')
		print(f'{homens} homens foram cadastrados.')
		print(f'E {mulheres} mulheres têm menos de 20 anos.')
		break