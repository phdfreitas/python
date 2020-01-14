#
# Created by Pedro Freitas on 13/01/2020.
#

from random import randint

nome = str(input('\033[1;37mPor favor, informe seu nome: '))
print('Vamos jogar PAR ou ÍMPAR.')

wins = 0

while True:
	playerChoice = int(input(f'{nome} o que você escolhe?\n[1] IMPAR\n[2] PAR\nSua resposta: '))

	player = int(input(f'Muito bem, {nome}. Agora escolha um número entre 0 e 10: '))
	cpu = randint(0, 10)

	total = player + cpu

	if (total % 2 == 0 and playerChoice == 1) or (total % 2 != 0 and playerChoice == 2):
		print(f'O total foi de {total}. Infelizmente {nome} você perdeu esta partida. Mais sorte da próxima vez.')
		break
	wins += 1
	
	print(f'O total é {total}, logo {nome} venceu esta partida. E até agora tem um total de {wins} vitória(s).')   