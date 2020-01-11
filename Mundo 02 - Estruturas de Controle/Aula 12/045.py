#
# Created by Pedro Freitas on 10/01/2020.
#

from random import choice
from time import sleep 

nome = str(input('\033[1;33mPor favor, informe o seu nome: ')).title()

print('Olá, meu nome é Christopher, muito prazer {}!'.format(nome))

resposta = str(input('Vamos jogar Jokenpô? Digite S para sim e N para não. ')).upper()

if resposta == 'S':
	print('Ótimo!! Então vamos jogar, {}.\nEu vou escolher primeiro, então você escolhe e daí mostramos o que escolhemos e vemos quem venceu, tudo bem?'.format(nome))
	resposta2 = str(input('Digite S para continuarmos e N caso não seja aceitável. ')).upper()	
	
	if resposta2 == 'S':
		print('Então vamos jogar!!!')

		christopher = choice(['Pedra', 'Papel', 'Tesoura'])
		jokenpo = str(input('Já escolhi, {}. Agora é sua vez, o que você escolhe: Pedra, Papel ou Tesoura? '.format(nome))).title()

		print('\nJoken...')
		sleep(3)
		print('PÔ!!\n')

		print('{} escolheu {} e Christopher escolheu {}'.format(nome, jokenpo, christopher))
		
		if christopher == jokenpo:
			print('\nEMPATE\nOra, ora, empatamos {}, vamos jogar de novo em outro momento. :)'.format(nome))
		elif (christopher == 'Pedra' and jokenpo == 'Tesoura') or (christopher == 'Tesoura' and jokenpo == 'Papel') or (christopher == 'Papel' and jokenpo == 'Pedra'):
			print('\nChristopher Vence!\nEu venci, {}! HAHA, mais sorte da próxima vez! :D'.format(nome))
		else:
			print('\nPedro Vence!\nHAHAHA, eu venci, Christopher. Eu sou o rei do Jokenpô!!!')
	else:
		print('Que pena :(\nEu gostaria de jogar com você {}. Até a proxima :('.format(nome))
else:
	print('Que pena :(\nEu gostaria de jogar com você {}. Até a proxima :('.format(nome))

#Não sei se ficou muito bom, mas eu tentei :)