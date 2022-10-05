idade = []
altura = []
for c in range(0, 5):
    idade.append(int(input("Digite a idade: ")))
    altura.append(float(input("Digite a altura: ")))
for c in range(0, 5):
    print(idade[len(idade)-1-c])
    print(altura[len(idade)-1-c])
