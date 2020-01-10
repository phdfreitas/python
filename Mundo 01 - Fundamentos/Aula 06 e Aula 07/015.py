#
# Created by Pedro Freitas on 31/12/2019.
#

km = float(input('Informe quantos KM foram percorridos: '))
dias = int(input('Por quantos dias o carro foi alugado? '))

total = (dias * 60) + (0.15 * km)

print('Percorrendo {}km e alugando o carro por {} dias o total a pagar é de R$ {:.2f}.'.format(km, dias, total))