'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

eighteen = men = womenTwenty = 0
while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    age = int(input('Idade: '))
    genre = continuation = ' '
    while genre not in 'FM':
        genre = str(input('Gênero: [F/M] ')).strip().upper()[0]
    print('-'*25)
    if age >= 18:
        eighteen += 1
    if genre == 'M':
        men += 1
    if genre == 'F' and age < 20:
        womenTwenty += 1
    while continuation not in 'SN':
        continuation = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuation == 'N':
        break
print(f'Total de {eighteen} pessoas com mais de 18 anos cadastradas.')
print(f'Total de {men} homens cadastrados.')
print(f'Total de {womenTwenty} mulheres com menos de 20 anos cadastradas.')
