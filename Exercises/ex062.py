'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA')
print('-=' * 20)
firstTerm = int(input('Primeiro termo: '))
ratio = int(input('Razão da PA: '))
term = firstTerm
counter = 1
moreTerms = 10
totalTerms = 0
while moreTerms != 0:
    totalTerms = totalTerms + moreTerms
    while counter <= totalTerms:
            print('{}'.format(term), end=' > ')
            term = term + ratio
            counter = counter + 1
    print('Pausa')
    moreTerms = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos exibidos.'.format(totalTerms))
