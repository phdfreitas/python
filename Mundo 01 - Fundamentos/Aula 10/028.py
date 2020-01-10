#
# Created by Pedro Freitas on 08/01/2020.
#

from random import randrange

userNumber = int(input('Choose a number from 0 to 5: '))
machineNumber = randrange(6) # Integer from 0 to 5  

if userNumber == machineNumber:
	print('User win! The number was {}'.format(userNumber))
else:
	print('Machine win! The correct number was {}'.format(machineNumber)) 