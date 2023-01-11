'''Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não
pode exceder 30% do salário ou então o empréstimo será negado.'''

price = float(input('Valor da casa: R$'))
wage = float(input('Salário do comprador: R$'))
time = int(input('Quantos anos de financiamento? '))
portion = price / (time * 12)
print(f'Para pagar uma casa de R${price:.2f} em {time} anos a prestação será de R${portion:.2f}.')
if portion <= 30 / 100 * wage:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
