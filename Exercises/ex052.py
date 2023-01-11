'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo.'''

value = int(input('Digite um número: '))
counter = 0

for c in range(1, value+1):
    if value % c == 0:
        counter += 1
        print(f'\033[31m{c}\033[m', end=' ')
    else:
        print(c, end=' ')

print(f'\nO número {value} foi divisível {counter} vezes!')

if counter == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
