'''Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não
pode exceder 30% do salário ou então o empréstimo será negado.'''

valor = float(input('Qual o valor do imóvel? R$'))
renda = float(input('Qual é o seu salário mensal? R$'))
prazo = int(input('Em quantos anos deseja pagar? '))
parcela = valor / (prazo*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, prazo, parcela))
if parcela <= renda * 30 / 100:
    print('Parabéns, seu empréstimo foi aprovado!')
else:
    print('Infelizmente seu empréstimo não foi aprovado!')
