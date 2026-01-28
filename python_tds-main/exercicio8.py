quntPares= 0
print('Contador de Números Pares')
print('Informe 5 números e descubra quantoas são pares:')
for i in range(5):
    numero = int(input(f'Informe o {i+1}º número: '))
    if numero % 2 == 0:
        quntPares += 1
print(f'A quantidade de números pares informados é: {quntPares}')