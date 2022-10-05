arquivo = int(input("digite o tamanho do arquivo em MB: "))
velocidade = int(input("digite a velocidade do download em Mbps: "))
tempo = arquivo / velocidade
minutos = tempo / 60
print(f"para fazer o download de um arquivo do tamanho {arquivo}MB com a velocidade de {velocidade}Mpbs levara"
      f" {minutos} minutos ")