#
# Created by Pedro Freitas on 13/01/2020.
#

stop = True
media = maior = menor = total = 0



while stop:
	n = float(input('\033[1;37mDigite um número: '))

	if total == 0:
		maior = n
		menor = n
		media = n
	else:
		media += n

		if n > maior:
			maior = n
		elif n < menor:
			menor = n
	total += 1

	r = str(input('Você quer continuar? [S/N]\nResposta: ')).upper()

	if r != 'S':
		stop = False
print('A média de todos os números digitados é {:.2f}'.format(media / total))
print('O MAIOR valor digitado foi {}\nE o MENOR foi {}'.format(maior, menor))