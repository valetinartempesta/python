def saluta(nome):
    saluto= f"Ciao, {nome}!"
    return saluto

def somma(a,b):
    return a+b

def saluta_antonio():
    return "Saluta Antonio"


messaggio=saluta("Alice")
print(messaggio)
print(somma(3,4))

globale =20 
def stampa_1():
    print(globale)
    globale=30
    print (globale)
    def stampa_2():
        print (globale)