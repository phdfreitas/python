#
# Created by Pedro Freitas on 11/01/2020.
#

frase = str(input('\033[1;33mDigite uma frase qualquer: ')).replace(' ', '').upper()

palindrome = 0

aux = len(frase) - 1

for c in range(0,len(frase)):
	if (frase[c] == frase[aux]):
		palindrome += 1
		aux -= 1

if(palindrome == len(frase)):
	print('É Palíndromo.')
else:
	print('Não é Palíndromo.')