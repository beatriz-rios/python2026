horas = int(input("Quantas horas você assiste por semana?"))
valor = int(input("Qual valor mensal da assinatura?"))

horas_mes = horas * 4 # proximando1 mes = 4 semanas
conta = valor / horas_mes

print(f"\nVocê assiste aparoxiamadamente {horas_mes:.1f} horas por mês.")
entreteniemento = print(f"Seu custo por hora de entreteniemento é: R${conta: .2f}")