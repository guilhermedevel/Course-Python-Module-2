'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

s = count = 0
for c in range(1, 7):
    number = int(input(f'Digite o {c}º valor: '))
    if number % 2 == 0:
        s += number
        count += 1
print(f'A soma dos {count} valores pares é {s}')
