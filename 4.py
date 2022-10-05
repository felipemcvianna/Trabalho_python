area = int(input("digite a area em metros quadrados a ser pintada: "))
litros = area / 3
precoLatas = 80
capacidadeL = 18
latas_necessarias = litros / capacidadeL
total = latas_necessarias * precoLatas
print(f"a quantidade de latas que voce vai precisar é de:{latas_necessarias:.0f}")
print(f"o valor a ser pago é de:R${total}")