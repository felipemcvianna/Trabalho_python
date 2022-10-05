peso = float(input("digite o peso do peixe : "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"o valor excedidos foi de {excesso}Kg portanto voce terá que pagar uma multa no valor de:R${multa:.2f}")