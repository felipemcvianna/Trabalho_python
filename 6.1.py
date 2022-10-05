Lista1 = []
Lista2 = []
lista3 = []
for posicao in range(0, 10):
    Lista1.append(int(input("digite os valores da primeira lista: ")))
for posicao in range(0, 10):
    Lista2.append(str(input("digite os valores da segunda lista: ")))
for posicao in range(0, 10):
    lista3.append(Lista1[posicao])
    lista3.append(Lista2[posicao])
print(lista3)