#
# Created by Pedro Freitas on 19/01/2020.
#

def maior(* numeros):
	print('=-=' * 30)
	print(f'Analisando os valores passados... {numeros}')
	print(f'Um total de {len(numeros)} números foram informados.\nE o maior deles é {max(numeros)}.')
	print('=-=' * 30)

maior(1, 2, 7, 40, 42, 43, 1025)
maior(1)
maior(1, 2, 7, 5)
maior(1, 43, 10, 25)