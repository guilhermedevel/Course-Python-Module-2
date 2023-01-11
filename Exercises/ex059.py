'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
firstValue = int(input('Digite um número: '))
secondValue = int(input('Digite mais um número: '))
userOption = 0
while userOption != 5:
    print('''Qual operação deseja realizar?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    userOption = int(input('Qual é a sua opção? '))
    if userOption == 1:
        sum = firstValue + secondValue
        print('{} + {} = {}'.format(firstValue, secondValue, sum))
    elif userOption == 2:
        multiply = firstValue * secondValue
        print('{} x {} = {}'.format(firstValue, secondValue, multiply))
    elif userOption == 3:
        larger = firstValue
        if secondValue > firstValue:
            larger = secondValue
        print('Entre {} e {} o maior é {}'.format(firstValue, secondValue, larger))
    elif userOption == 4:
        firstValue = int(input('Digite um número: '))
        secondValue = int(input('Digite mais um número: '))
    elif userOption == 5:
        print('Obrigado! Finalizando...')
    else:
        print('Opção inválida. Selecione uma opção entre 1 e 5.')
    print('=-=' * 16)
    sleep(2)
print('Programa encerrado.')
