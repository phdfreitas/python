#
# Created by Pedro Freitas on 05/01/2020.
#

import math

ang = float(input('DIgite o valor de um ângulo: '))

sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('Os valores do seno, cosseno e tangente são respectivamente:\nSeno: {:.2f},\nCosseno: {:.2f},\nTangente: {:.2f}.'.format(sin, cos, tan))