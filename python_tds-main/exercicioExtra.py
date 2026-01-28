print('Simulador de Saldo Bancário')
print('Informe se quer sacar ou depositar, e o valor que estiver depositando ou sacando: ')
Saq_Dep = input('Digite "saque" para sacar ou "deposito" para depositar:')
saldo = 0
if Saq_Dep == 'deposito':
    valor1 = float(input('Digite o valor que deseja depositar:'))
    saldo += valor1
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
elif Saq_Dep == 'saque':
    valor2 = float(input('Digite o valor que deseja sacar:'))
    if valor2 > saldo:
        print('Saldo insuficiente para saque.')
    else:
        saldo -= valor2
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
