palavra = (input("Digite a palavra secreta: "))
print("Palavra revelando...")
for indice in range (len(palavra)):
    letra = palavra[indice]
    posicao = indice +1
    print(f"{posicao} - {letra}")