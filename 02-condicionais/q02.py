velocidade = float(input("Informe a velocidade"))

multa = (velocidade-80)*7

if velocidade >80:
    print("O valor de sua multa é de: R$", multa)
else:
    print("Velocidade permitida, sem multas")