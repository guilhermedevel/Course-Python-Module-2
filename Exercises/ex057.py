'''Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

genre = str(input('Informe seu gênero (F/M): ')).strip().upper()[0]
while genre not in 'FfMm':
    genre = str(input('Dados inválidos. Por favor, informe seu gênero (F/M): ')).strip().upper()[0]
print('Gênero {} registrado com sucesso!'.format(genre))
