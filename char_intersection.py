frase1 = input(str())
frase2 = input(str())

palavras1 = set(frase1.split())
palavras2 = set(frase2.split())

intersecao = palavras1 & palavras2
print(intersecao)

palavras = []
pontuacao = []
for palavra in intersecao:
    if palavra[0].isalpha():
        palavras.append(palavra)
    else:
        pontuacao.append(palavra)

palavras_ordenadas = sorted(palavras) +sorted(pontuacao)
print(" ".join(palavras_ordenadas))