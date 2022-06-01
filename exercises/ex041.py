'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

nascimento = int(input('Ano do nascimento: '))
from datetime import date
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade < 15:
    print('Classificação: INFANTIL.')
elif idade < 20:
    print('Classificação: JÚNIOR.')
elif idade < 26:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')
