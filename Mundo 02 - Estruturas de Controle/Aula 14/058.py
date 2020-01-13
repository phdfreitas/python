#
# Created by Pedro Freitas on 13/01/2020.
#

from random import randrange

nome = str(input('\033[1;33mAntes de começarmos o jogo digite seu nome: ')).title()

stop = True # variavel de parada do while
palpites = 0

while stop:
	palpites += 1

	userNumber = int(input('Escolha um número entre 0 e 10: '))
	machineNumber = randrange(11) # "escolhe" um número entre 0 e 10  

	if userNumber == machineNumber:
		print('{} venceu! O número correto era {}. Ele tentou um total de {} vezes.'.format(nome, userNumber, palpites))
		stop = False
	else:
		print('A máquina venceu! O número correto era {}. Tente novamente, {}.'.format(machineNumber, nome))