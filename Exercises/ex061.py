'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('Gerador de PA')
print('-=' * 20)
firstTerm = int(input('Primeiro termo: '))
ratio = int(input('Razão da PA: '))
term = firstTerm
counter = 0
while counter < 10:
        print('{}'.format(term), end=' > ')
        term = term + ratio
        counter = counter + 1
print('Acabou!')
