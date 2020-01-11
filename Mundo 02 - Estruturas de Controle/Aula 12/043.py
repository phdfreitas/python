#
# Created by Pedro Freitas on 09/01/2020.
#

peso = float(input('\033[1;33mDigite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura**2)

if imc < 18.5:
	print('Abaixo do peso ideal. Seu IMC é {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
	print('Você está no peso ideal. Seu IMC é {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
	print('Você está obeso. Seu IMC é {:.2f}'.format(imc))
else:
	print('Você está com obesidade morbida. Seu IMC é {:.2f}'.format(imc))