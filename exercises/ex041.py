'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date

birth = int(input('Ano de nascimento: '))
currentYear = date.today().year
age = currentYear - birth

print(f'O atleta tem {age} anos.')
print('Classificação: ', end='')
if age <= 9:
    print('MIRIM')
elif 9 < age <= 14:
    print('INFANTIL')
elif 14 < age <= 19:
    print('JÚNIOR')
elif 19 < age <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
