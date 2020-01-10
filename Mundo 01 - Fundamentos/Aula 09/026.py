#
# Created by Pedro Freitas on 08/01/2020.
#

sentence = str(input('Enter a sentence: ')).upper().strip()

print('Count "A": {}'.format(sentence.count('A')))
print('First "A": {}'.format(sentence.find('A') + 1))
print('Last "A": {}'.format(sentence.rfind('A') + 1))