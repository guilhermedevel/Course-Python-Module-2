'''Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se
já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

birth = int(input('Ano de nascimento: '))
currentYear = date.today().year
age = currentYear - birth

print(f'Quem nasceu em {birth} tem {age} anos em {currentYear}.')

if age < 18:
    diference = 18 - age
    print(f'Ainda faltam {diference} anos para o seu alistamento.')
    print(f'Seu alistamento será em {currentYear + diference}.')
elif age > 18:
    diference = age - 18
    print(f'Você já deveria ter se alistado há {diference} anos.')
    print(f'Seu alistamento foi em {currentYear - diference}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')