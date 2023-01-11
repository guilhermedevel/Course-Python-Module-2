'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

sum = thousand = counter = cheap = 0
cheapName = ' '
while True:
    product = str(input('Nome do produto: '))
    price = int(input('Preço: R$'))
    sum += price
    if price > 1000:
        thousand += 1
    counter += 1
    if counter == 1 or price < cheap:
        cheap = price
        cheapName = product
    continuation = ' '
    while continuation not in 'SN':
        continuation = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuation == 'N':
        break
print(f'O total da compra foi de R${sum:.2f}')
print(f'Temos {thousand} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {cheapName} que custa R${cheap:.2f}')
