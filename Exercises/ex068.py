'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
from random import randint
wins = 0
while True:
    computer = randint(0, 10)
    user = int(input('Jogue um número: '))
    sum = computer + user
    choice = ' '
    while choice not in 'PI':
        choice = str(input('Você escolhe par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {user} e o computador jogou {computer}. Total de {sum}, ', end='')
    if choice == 'P':
        if sum % 2 == 0:
            print('deu PAR, você VENCEU!')
            wins += 1
        else:
            print('deu ÍMPAR, você PERDEU!')
            break
    elif choice == 'I':
        if sum % 2 == 1:
            print('deu ÍMPAR, você VENCEU!')
            wins += 1
        else:
            print('deu PAR, você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Total de {wins} vitórias.')
