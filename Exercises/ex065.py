'''Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final
da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

continuation = 'S'
sum = counter = larger = smaller = 0
while continuation in 'S':
    number = int(input('Digite um número: '))
    continuation = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    sum = sum + number
    counter = counter + 1
    if counter == 1:
        larger = smaller = number
    else:
        if number > larger:
            larger = number
        elif number < smaller:
            smaller = number
average = sum / counter
print('Você digitou {} números e a média foi de {:.2f}'.format(counter, average))
print('O maior valor foi {} e o menor foi {}'.format(larger, smaller))
