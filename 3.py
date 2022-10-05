ganho_por_hora = float(input("digite o quanto voce ganha por hora: "))
horas_trabalhadas = int(input("digite as suas horas trabalhadas no mes: "))
salario_bruto = ganho_por_hora * horas_trabalhadas
print(f"o seu salario bruto é de:R${salario_bruto}")
INSS = (salario_bruto * 8) / 100
print(f"seu desconto do INSS é de:R${INSS}")
Sindicato = (salario_bruto * 5) / 100
print(f"o desconto do sindicato é de:R${Sindicato}")
Imposto_Renda = (salario_bruto * 11) / 100
print(f"o seu desconto do imposto de renda é de:R${Imposto_Renda}")
salario_liquido = salario_bruto - Sindicato - INSS - Imposto_Renda
print(f"o seu salario com os descontos é de:R${salario_liquido:.2f}")
