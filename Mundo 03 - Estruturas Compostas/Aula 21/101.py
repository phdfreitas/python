#
# Created by Pedro Freitas on 20/01/2020.
#

def voto(ano):
	from datetime import date
	anoAtual = date.today().year
	idade = anoAtual - ano

	if idade >= 18 and idade <= 65:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
	elif (idade >= 16 and idade < 18) or idade > 65:
		return f'Com {idade} anos: VOTO OPCIONAL!'
	else:
		return f'Com {idade} anos: NÃO VOTA!'

anoNascimento = int(input('Digite o ano em que você nasceu: '))
print(voto(anoNascimento))