print('Operação de Divisão')
while True:
    n1 = int(input('Informe o priemeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    if n2 == 0:
        print('Divisor não pode ser 0. Tente novamente.')
        break
    print(f"{n1} / {n2} = {(n1/n2):.2f}")
    print('Fim da Operação de Divisão')