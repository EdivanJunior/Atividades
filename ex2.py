ano = int(input("Digite o ano atual:"))

dataNascimento = int(input("Digite o ano que você nasceu:"))

valor = ano - dataNascimento
print("RESULTADO:")

print (valor)

if valor >= 18:
    print ("VOCÊ ESTÁ APTO A VOTAR!")
else:
    print("AGUARDE A MAIOR IDADE!")




