camisa = 12.50
quant = int(input("Quantas camisas você vai levar?"))
valor = quant * camisa

if quant <= 5:
 print(f" O preço da camisa é: {valor * 0.97:.2f}")
elif  quant <= 10:
    print (f"O preço da camisa é: {valor * 0.95:.2f}")    
else:
    (f"O preço da camisa é: {camisa * 0.93:.2f}")
