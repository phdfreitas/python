#
# Created by Pedro Freitas on 10/01/2020.
#

produto = float(input('\033[1;33mDigite o preço do produto: '))

pagamento = str(input("""Qual a forma de pagamento? 
	\n1. À Vista Dinheiro/Cheque
	\n2. À vista no cartão
	\n3. Até 2x no cartão
	\n4. Em 3x ou mais no cartão
	\nSua resposta: """))

if pagamento == '1':
	print('O produto custa R$ {:.2f}, porém você receberá "10%" de desconto e vai pagar R$ {:.2f}'.format(produto, (produto * 0.9)))
elif pagamento == '2':
	print('O produto custa R$ {:.2f}, porém você receberá "5%" de desconto e vai pagar R$ {:.2f}'.format(produto, (produto * 0.95)))
elif pagamento == '3':
	print('O produto custa R$ {:.2f}, porém você NÃO receberá desconto e vai pagar R$ {:.2f}'.format(produto, produto))
else:
	print('O produto custa R$ {:.2f}, porém você sofrerá "20%" de juros e vai pagar R$ {:.2f}'.format(produto, (produto * 1.20)))