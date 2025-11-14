frase = input("Digite uma frase: ")

dic = {}

for caractere in frase:

    if caractere == " ":
        continue

    if caractere in dic:
        dic[caractere] += 1
    else:
        dic[caractere] = 1

print(dic)
