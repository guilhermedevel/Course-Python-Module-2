'''Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N
primeiros elementos de uma Sequência de Fibonacci. '''

print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
terms = int(input('Quantos termos você quer ver? '))
firstTerm = 0
secondTerm = 1
print('{} > {} > '.format(firstTerm, secondTerm), end='')
counter = 3
while counter <= terms:
    thirdTerm = firstTerm + secondTerm
    print('{} > '.format(thirdTerm), end='')
    firstTerm = secondTerm
    secondTerm = thirdTerm
    counter = counter + 1
print('Acabou!')
