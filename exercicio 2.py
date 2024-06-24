numero = int(input('digite o numero da tabuada'))
print('tabuada do', numero)

for i in range(1,11):
    resultado = numero * i #soma do numero  mais i que dara avariavel resutado
    print('{}x{} = {}'.format(numero,i,resultado))