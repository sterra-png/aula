nome = str(input('qual o seu nome'))

p1 = float(input('Qual foi sua nota de português?'))
m2 = float(input('Qual sua nota de matemática?'))
c3 = float(input('Qual sua nota de ciências?'))
b4 = float(input('Qual sua nota de biologia?'))

media = (p1 + m2 + c3 + b4) / 4

print('prazer {} sua media é {}'.format(nome,media))