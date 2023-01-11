'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''

import emoji
from random import randint
from time import sleep

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

plays = ['Pedra', 'Papel', 'Tesoura']
computer = plays[randint(0, 2)]
player = int(input('Qual é a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=' * 15)
print(f'Computador jogou {computer}.')
print(f'Jogador jogou {plays[player]}.')
print('-=' * 15)

if player == 0:     #Jogador escolhendo Pedra
    if computer == 'Papel':
        print('Jogador perde! ', end='')
        print(emoji.emojize(':weary:', language='alias'))
    elif computer == 'Tesoura':
        print('Jogador vence! ', end='')
        print(emoji.emojize(':satisfied:', language='alias'))
    else:
        print('Empate! ', end='')
        print(emoji.emojize(':unamused:', language='alias'))
elif player == 1:    #Jogador escolhendo Papel
    if computer == 'Pedra':
        print('Jogador vence! ', end='')
        print(emoji.emojize(':satisfied:', language='alias'))
    elif computer == 'Tesoura':
        print('Jogador perde! ', end='')
        print(emoji.emojize(':weary:', language='alias'))
    else:
        print('Empate! ', end='')
        print(emoji.emojize(':unamused:', language='alias'))
elif player == 2:    #Jogador escolhendo Tesoura
    if computer == 'Pedra':
        print('Jogador perde! ', end='')
        print(emoji.emojize(':weary:', language='alias'))
    elif computer == 'Papel':
        print('Jogador vence !', end='')
        print(emoji.emojize(':satisfied:', language='alias'))
    else:
        print('Empate! ', end='')
        print(emoji.emojize(':unamused:', language='alias'))