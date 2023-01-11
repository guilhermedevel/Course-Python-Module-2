'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

number = counter = sum = 0
while not number == 999:
    number = int(input('Digite um número [999 para parar]: '))
    if number != 999:
        counter = counter + 1
        sum = sum + number
print('Você digitou {} números e a soma entre eles foi {}. Programa finalizado.'.format(counter, sum))
