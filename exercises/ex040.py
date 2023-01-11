'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

firstTest = float(input('Primeira nota: '))
secondTest = float(input('Segunda nota: '))
average = (firstTest + secondTest) / 2

print(f'Com as notas {firstTest} e {secondTest}, a média do aluno é de {average}!')

if average < 5:
    print('O aluno está REPROVADO.')
elif 5 <= average < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno foi APROVADO.')
