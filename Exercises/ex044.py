'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

price = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

payment = int(input('Qual a forma de pagamento? '))

if payment == 1:
    discount = price * 10/100
    newPrice = price - discount
    print(f'Sua compra de R${price:.2f} vai custar R${newPrice:.2f} no final.')
elif payment == 2:
    discount = price * 5/100
    newPrice = price - discount
    print(f'Sua compra de R${price:.2f} vai custar R${newPrice:.2f} no final.')
elif payment == 3:
    print(f'Sua compra será parcelada em 2x de R${price/2} sem juros.')
    print(f'Sua compra de R${price:.2f} continuará R${price:.2f} no final.')
elif payment == 4:
    fees = price * 20/100
    newPrice = price + fees
    portion = int(input('Quantas parcelas? '))
    portionPrice = newPrice / portion
    print(f'Sua compra será parcelada em {portion}x de R${portionPrice:.2f} com juros.')
    print(f'Sua compra de R${price:.2f} vai custar R${newPrice:.2f} no final.')
else:
    print('Opção inválida!')