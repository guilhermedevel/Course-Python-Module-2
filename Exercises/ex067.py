'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''

while True:
    number = int(input('Digite um número para ver sua tabuada: '))
    if number < 0:
        break
    multiplier = 1
    while multiplier <= 10:
        print(f'{number} x {multiplier:2} = {number * multiplier:2}')
        multiplier += 1
