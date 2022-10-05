import math
litros_por_lata = 18
preco_lata = 80
litros_por_galao = 3.6
preco_galao = 25
area = float(input("digite a area em metros quadrados a ser pintada: "))
area_com_folga = area * 1.1
litros_necessarios = area_com_folga / 6
qtd_latas = math.ceil(litros_necessarios / litros_por_lata)
print(f" a quantidade de latas usadas sera {qtd_latas}")
valor_latas = qtd_latas * preco_lata
print(f"o valor na compra de {qtd_latas} latas de tinta é de:R${valor_latas:.2f}")

qtd_galoes = math.ceil(litros_necessarios / litros_por_galao)
print(f"a quantidade de galoes usados sera de:{qtd_galoes}")
valor_galoes = qtd_galoes * preco_galao
print(f"o valor na compra de {qtd_galoes} galoes de tinta sera de:R${valor_galoes:.2f}")

numero_de_latas = math.floor(litros_necessarios / litros_por_lata)
valor_de_latas = numero_de_latas * preco_lata
litros_restantes = litros_necessarios % litros_por_lata
numero_de_galoes = math.ceil(litros_restantes / litros_por_galao)
valor_com_galoes = numero_de_galoes * preco_galao
valor_total = valor_de_latas + valor_com_galoes
print(f"voce devera usar {numero_de_latas} latas e {numero_de_galoes} galoes, no valor de {valor_total}")