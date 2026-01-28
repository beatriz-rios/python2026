tensao = int(input('Digite o valor da tensão da fonte de alimentação em volts: '))
dispositivo = int(input('Digite o valor da potência do dispositivo em volts: '))
amperes = int(input('Digite o valor da corrente em Amperes: '))

resistencia = (tensao - dispositivo) / amperes
print(f'O valor da resistência necessária é: {resistencia} Ohms')