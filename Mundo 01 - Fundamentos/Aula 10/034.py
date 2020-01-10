#
# Created by Pedro Freitas on 08/01/2020.
#

salary = float(input('Enter your salary: R$ '))

if salary > 1250:
	print('O aumento no salário vai ser de 10%, assim o seu novo salário é R$ {:.2f}'.format(salary + (salary * 0.1)))
else:
	print('O aumento no salário vai ser de 15%, assim o seu novo salário é R$ {:.2f}'.format(salary + (salary * 0.15)))