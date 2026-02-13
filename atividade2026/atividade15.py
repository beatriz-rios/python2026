produto = {
    1: "Monitor LED 24 - R$599.99 1un",
    2: "Teclado Wireless - R$49.26 - 1un",
    3: "Mouse Wireless - R$19.90 - 1un",
    4: "Cartucho colorido - R$54.00 2un"
}

print("Produtos Disponíveis")
for chave, info in produto.items():
    print(f"{chave}: {info}")

total = 0

while True:
    
        escolha = int(input('\nDigite o número do produto (ou 0 para finalizar): '))
        if escolha == 0:
            break
            
        if escolha in produto:
            quantd = int(input(f"Digite a quantidade para '{produto[escolha]}': "))
            texto_preco = produto[escolha].split("R$")[1].strip().split()[0]
            valor_produto = float(texto_preco)
            subtotal = valor_produto * quantd
            total += subtotal
            print(f"Adicionado! Subtotal: R${subtotal:.2f}")
        else: 
            print("Produto não encontrado. Tente novamente.")
            
    

print("-" * 30)
print(f"VALOR TOTAL DA COMPRA: R${total:.2f}")
print("Obrigado pela preferência!")