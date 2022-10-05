altura = float(input("digite a altura do individuo: "))
sexo = str(input("digite o sexo do individuo(M para masculino ou F para feminino): "))

if sexo == "M":
    Peso_ideal = (72.7*altura)-58
    print("seu peso ideal é:{:.2f}".format(Peso_ideal))
if sexo == "F":
    Peso_ideal = (62.1*altura) - 44.7
    print("o seu peso ideal é: {:.2f}".format(Peso_ideal))
