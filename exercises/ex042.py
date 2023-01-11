'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

<<<<<<< Updated upstream
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a <= b + c and b <= a + c and c <= a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a != b != c != a:
        print('ESCALENO.')
    else:
=======
print('-=' * 30)
print('Analisador de triângulos 1.0')
print('-=' * 30)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l2 + l3 > l1 > l2 - l3 and l1 + l3 > l2 > l1 - l3 and l1 + l2 > l3 > l1 - l2:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
>>>>>>> Stashed changes
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
