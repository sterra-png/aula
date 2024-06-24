frutas = ['banana,','maça','pera','laranja']
alergias = ['mel','abacaxi','abacati','melancia']

alergias.append('alaba')
print(frutas)
print(alergias)

for frutas in frutas:
    if frutas in alergias:
        print(f"A fruta '{frutas}' está na lista de alergias.")
