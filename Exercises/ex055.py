'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
e o menor peso lidos.'''

larger = smaller = 0
for c in range(1, 6):
    weight = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        larger = smaller = weight
    else:
        if weight > larger:
            larger = weight
        elif weight < smaller:
            smaller = weight
print(f'O maior peso lido foi de {larger}Kg')
print(f'O menor peso lido foi de {smaller}Kg')
