#
# Created by Pedro Freitas on 13/01/2020.
#

from time import sleep

n1 = float(input('\033[1;33mDigite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

stop = True

while stop:
	resposta = int(input("""\033[1;33mO que você deseja fazer?
[1] Somar os números informados
[2] Multiplicar os números informados
[3] Maior entre os números informados
[4] Novos números
[5] Sair do programa
Resposta: """))

	if resposta == 1:
		print('\033[1;37mA soma entre {} e {} é {}'.format(n1, n2, (n1 + n2)))
	elif resposta == 2:
		print('\033[1;37mO produto entre {} e {} é {}'.format(n1, n2, (n1 * n2)))
	elif resposta == 3:
		if n1 > n2:
			print('\033[1;37mO Maior entre {} e {} é {}'.format(n1, n2, n1))
		elif n2 > n1:
			print('\033[1;37mO Maior entre {} e {} é {}'.format(n1, n2, n2))
		else: 
			print('\033[1;37mOs dois valores informados são iguais.')
	elif resposta == 4:
		print('\033[1;37mDigite novos números: ')

		n1 = float(input('Digite o primeiro valor: '))
		n2 = float(input('Digite o segundo valor: '))
	else:
		print('\033[1;37mVocê está saindo do programa...')
		sleep(2)
		print('\033[1;37mAté a próxima.')
		stop = False