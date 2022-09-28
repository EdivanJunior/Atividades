convidados = [
    "Coringa", "Thor","Jesus","Naruto","Loki"
]

# Convite
for nome in convidados:   
    mensagen = f"Bora pra balada,{nome}"
    print (mensagen)

# Quem nao podera ir
print ("Jesus: Infelizmente não posso estar no mesmo ambiente que o Loki!")

print ("Coringa: Infelizmente não posso estar no mesmo ambiente que o Naruto!")

# Modifique sua lista, substitua os
# desistentes por novos convidados.
convidados[2] = "Madre Tereza"
convidados[0] = "Pinguin"

for nome in convidados:   
    mensagen = f"Bora pra balada,{nome.upper()}!"
    print (mensagen)