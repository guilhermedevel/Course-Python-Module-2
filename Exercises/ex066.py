'''Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

counter = sum = 0
while True:
    number = int(input('Digite um valor: '))
    if number == 999:
        break
    counter += 1
    sum += number
print(f'Você digitou {counter} números e a soma entre eles é {sum}!')
