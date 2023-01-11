'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

weight = float(input('Qual é o seu peso? (Kg) '))
height = float(input('Qual é a sua altura? (m) '))
bmi = weight / height ** 2

print(f'O IMC dessa pessoa é de {bmi:.1f}')

if bmi < 18.5:
    print('Cuidado! Você está abaixo do peso ideal.')
elif 18.5 <= bmi < 25:
    print('Parabéns! Você está no peso ideal.')
elif 25 <= bmi < 30:
    print('Cuidado! Você está em sobrepeso.')
elif 30 <= bmi < 40:
    print('Procure um médico, você está com obesidade.')
else:
    print('Procure um médico URGENTE, você está com obesidade mórbida.')