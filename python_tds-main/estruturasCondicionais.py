print(f'programa de empréstimos.'
      f'Responda: (0-não ou 1-sim)')

nome_negativado = int(input('Possui nome negativado?'))
if nome_negativado == 1: #sim
    print('Não pode realizar empréstimo')
else:
    carteira_assinada = int(input('Possui carteira assinada?'))
    if carteira_assinada == 0: #não
        print('Não pode realizar empréstimo')
    else:
        possui_casa_propria = int(input('Possui casa própria?'))
        if possui_casa_propria == 0: #não
            print('Não pode realizar empréstimo')
        else:
            print('Conceder empréstimo')