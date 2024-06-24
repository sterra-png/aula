def verificar_email (email):
    dominio = '@jogajuntoinstituto.org'
    if dominio in email:
        return True
    else:
        return False
    
email = input('coloque seu email')

if verificar_email(email):
        print('email valido')
else:
        print('email invalido')