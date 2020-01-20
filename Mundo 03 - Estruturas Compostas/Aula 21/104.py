def leiaInt(num):
	valor = 0
	ok = False
	while True:
		n = str(input(num))
		if n.isnumeric():
			valor = int(n)
			ok = True
		else:
			print('ERRO! Digite um número inteiro válido.')

		if ok:
			break
	return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')