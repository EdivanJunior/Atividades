print ("[!]PROMOÇÃO[!]")
print ("Maçãs por 1,30r$ ou acima de 12 por apenas 1,00r$ !")

maças = int(input("Digite quantas maçãs você quer comprar:"))

preçoPromoção = 1.00
preçoComum = 1.30

valorPromoção = maças * preçoPromoção
valorComum = maças * preçoComum


print ("VALOR A PAGAR:")
if maças >= 12:
    print (valorPromoção)
elif maças <= 11:
    print(valorComum)


