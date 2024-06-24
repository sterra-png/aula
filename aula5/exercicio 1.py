idade = int(input('qual a sua idade ?'))

if idade >= 18:
    print('Indivíduo possui idade para dirigir')

elif 17 <= idade <18:
    print('divíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir')

else:
    print('Indivíduo NÃO possui idade mínima para dirigir')