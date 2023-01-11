'''Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

number = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

choice = int(input('Sua opção: '))

if choice == 1 or choice == 2 or choice == 3:
    print(f'{number} convertido para ', end='')
    if choice == 1:
        print(f'BINÁRIO é igual a {bin(number)[2:]}')
    elif choice == 2:
        print(f'OCTAL é igual a {oct(number)[2:]}')
    elif choice == 3:
        print(f'HEXADECIMAL é igual a {hex(number)[2:]}')
else:
    print('Opção inválida! Tente novamente.')
