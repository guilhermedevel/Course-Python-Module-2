'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

firstTerm = int(input('Primeiro termo: '))
ratio = int(input('Razão da PA: '))
tenthTerm = firstTerm + 10 * ratio
for c in range(firstTerm, tenthTerm, ratio):
    print(c, end=' > ')
print('Acabou')

