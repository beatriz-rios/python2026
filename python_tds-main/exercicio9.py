print('Sistema de Login')
print('Caso errar a senha na primeira tentativa, terá mais 2 chances.')
senha = 123456
chance = 3

while True :
    tentativa = int(input('Digite sua senha:'))
    if tentativa == senha:
        print('Acesso Permitido.')
        break
    else:
        chance -= 1
        if chance <= 0:
            print('Sua senha foi bloqueada!Por favor, dirija-se a um de nossos caixas')
            break
        else:
            print('senha incorreta.Tem mais', chance, 'tentativas.')