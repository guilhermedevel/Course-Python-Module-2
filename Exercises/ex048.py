'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.'''

sum = counter = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        sum += c
        counter += 1
print(f'A soma de todos os {counter} valores solicitados é de {sum}.')
