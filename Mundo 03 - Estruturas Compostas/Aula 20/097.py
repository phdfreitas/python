#
# Created by Pedro Freitas on 18/01/2020.
#

def escreva(txt):
	print('~' * len(txt))
	print(txt)
	print('~' * len(txt))

texto = str(input('Digite uma mensagem: '))
escreva(texto)