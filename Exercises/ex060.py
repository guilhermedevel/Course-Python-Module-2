'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

number = int(input('Digite um número para calcular seu fatorial: '))
factorial = 1
print('Calculando {}! = '.format(number), end='')
while number > 0:
    print(number, end='')
    print(' x ' if number > 1 else ' = ', end='')
    factorial = factorial * number
    number = number - 1
print(factorial)
