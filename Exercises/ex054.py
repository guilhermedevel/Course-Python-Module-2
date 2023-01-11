'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

minority = majority = 0
currentYear = date.today().year

for c in range(1, 8):
    birth = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    age = currentYear - birth
    if age >= 18:
        majority += 1
    else:
        minority += 1
print(f'Ao todo tivemos {majority} pessoas maiores de idade.')
print(f'E também tivemos {minority} pessoas menores de idade.')
