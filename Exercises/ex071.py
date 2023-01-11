'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

cash = int(input('Qual valor você quer sacar? R$'))
totalCash = cash
note = 50
totalNotes = 0
while True:
    if totalCash >= note:
        totalCash -= note
        totalNotes += 1
    else:
        if totalNotes > 0:
            print(f'Total de {totalNotes} cédulas de R${note}')
        totalNotes = 0
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 1
        if totalCash == 0:
            break
print('Operação finalizada. Obrigado e volte sempre!')
