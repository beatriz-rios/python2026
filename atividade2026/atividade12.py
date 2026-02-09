print("Digite 5 números inteiros: ")
numeros = []
for i in range(5):
    input_numero = int(input(f"Número {i + 1}:"))
    numeros.append(input_numero)
print("Números digitados : ", numeros)
soma = sum(numeros)
print("A soma dos números é: ", soma)
maior = max(numeros)
print("O maior número é:", maior)
menor = min(numeros)
print("O menor número é:", menor)
media = soma / len(numeros)
print("A média dos números é: ", media)