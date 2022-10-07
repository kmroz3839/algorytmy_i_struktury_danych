
def z1(pli, nazw):
    return pli+". " + nazw

def z2(imie: str, nazwisko: str):
    return imie[:1].upper() + ". " + nazwisko[:1].upper() + nazwisko[1:].lower()

print(z2("michał", "morbiusz"))

def z3(a: int,b: int,wiek: int):
    aktualny_rok = a * 100 + b
    return aktualny_rok - wiek

print(z3(20,22,20))

def z4(imie, nazwisko,funkcja):
    return funkcja(imie,nazwisko)

print(z4("michał", "morbiusz", z2))

def z5(a, b):
    if a>0 and b>0 and b != 0:
        return a/b
    return -1

print(z5(3,2))

def z6():
    suma = 0
    while suma < 100:
        suma += int(input())
        print(suma)

#z6()

def z7(lista: list):
    return tuple(lista)

a = [2,3,4,5,39,40]
print(z7(a))

def z8():
    l = []
    for x in range (1,10): #załóżmy
        l.append(float(input()))  #załóżmy
    return tuple(l)

#print(z8())

def z9(a: int):
    dt = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
    return dt[a-1]

print(z9(6))

def z10(arg: str):
    for x in range(0, int(len(arg)/2)):
        if arg[x] != arg[len(arg)-1-x]:
            return False
    return True

print(z10("ABCCBA"))
print(z10("AMOGUS"))