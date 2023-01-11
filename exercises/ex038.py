'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na
tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''

firstNumber = int(input('Primeiro número: '))
secondNumber = int(input('Segundo número: '))

if firstNumber > secondNumber:
    print('O PRIMEIRO valor é maior.')
elif firstNumber < secondNumber:
    print('O SEGUNDO valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
