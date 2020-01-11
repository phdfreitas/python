#
# Created by Pedro Freitas on 09/01/2020.
#

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if media < 5:
	print('Sua média foi {:.2f}. Infelizmente você foi reprovado.'.format(media))
elif media >= 5 and media < 7:
	print('Sua média foi {:.2f}. Infelizmente você está na recuperação, mas ainda há esperança.'.format(media))
else:
	print('Sua média foi {:.2f}. Parabéns, você foi aprovado por média.'.format(media))	
