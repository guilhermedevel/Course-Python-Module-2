'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é
um palíndromo, desconsiderando os espaços.'''

phrase = str(input('Digite uma frase curta: ')).upper().strip()
split = phrase.split()
join = ''.join(split)
reverse = ''

for c in range(len(join)-1, -1, -1):
    reverse += join[c]

print(f'O inverso de {join} é {reverse}')

if reverse == join:
    print('Temos um PALÍNDROMO!')
else:
    print('Não temos um PALÍNDROMO!')
