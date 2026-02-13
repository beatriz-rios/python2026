print('Lista Organizadora de Mercadorias')
lista = []
while True:
    produto = input('Digite o nome do produto (ou "0" para encerrar): ')
    if produto.lower() == '0':
        break
    quantidade = int(input('Digite a quantidade do produto: '))
    lista.append([produto, quantidade]) 
print("\nLista de Compras:")
for item in lista:
    print(f"Produto: {item[0]}, Quantidade: {item[1]}")