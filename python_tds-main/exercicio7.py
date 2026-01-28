print('Contador de Números')
n1 = print('Informe a quantidade de números que deseja contar para descobrir a média entre eles:')
n = int(input())
soma = 0
for i in range(n):
    numero = int(input(f'Informe o {i+1}º número: '))
    soma = soma + numero
    media = soma / n
print(f'A média dos {n} números informados é: {media}')
