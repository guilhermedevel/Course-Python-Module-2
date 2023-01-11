'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.'''

addAge = older = counter = nameOlder = womenUnder = 0

for c in range(1, 5):
    print(f'{"-"*5} {c}ª PERSON {"-"*5}')
    name = str(input('Name: ')).strip().capitalize()
    age = int(input('Age: '))
    genre = str(input('Genre [F/M]: ')).upper()[0].strip()
    addAge += age
    if genre == 'M':
        counter += 1
        if counter == 1:
            older = age
            nameOlder = name
        else:
            if age > older:
                older = age
                nameOlder = name
    else:
        if age < 20:
            womenUnder += 1

average = addAge / 4
print(f'A média de idade do grupo é de {average} anos.')
print(f'O homem mais velho do grupo é o {nameOlder} com {older} anos.')
if womenUnder != 0:
    print(f'Temos um total de {womenUnder} mulheres com menos de 20 anos.')