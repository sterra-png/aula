palavra = input("Digite uma palavra: ")
   
vogais = "aeiouAEIOU"
    
contador = 0
    
for i in palavra:
        if i in vogais:
            contador += 1
    

print("O número de vogais na palavra {}".format(contador))
