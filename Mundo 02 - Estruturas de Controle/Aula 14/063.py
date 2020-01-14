#
# Created by Pedro Freitas on 13/01/2020.
#

n = int(input('\033[1;37mDigite um número inteiro: '))

contador = first = 0
aux = fib = 1 

print(first, end=' ')

while contador < n:
	print(fib, end=' ')
	if contador == 0:
		fib = first + aux # 0 + 1 = 1
	elif contador == 1:
		fib = fib + aux # 1 + 1 = 2
	else:
		aux = fib - aux
		fib = fib + aux
	contador += 1
print() 