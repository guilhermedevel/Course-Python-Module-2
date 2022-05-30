'''Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é a igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')
