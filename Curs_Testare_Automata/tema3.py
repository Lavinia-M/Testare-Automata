# Exercitiul 1
"""Functia de tip if else este de tip flow control, evalueaza conditiile puse, apoi parcurge codul si se opreste
in functie de conditiile date. """

# Exercitiul 2
x = input(f"Introdu un numar: ")
if x.isdigit():
    print(f"Nr {x} este un nr natural")
else:
    print(f"Nr {x} nu este natural")

# Exercitiul 3
x = int(x)
if x > 0:
    print(f"Nr {x} este pozitiv")
elif x < 0:
    print(f"Nr {x} este negativ")
else:
    print(f"Nr {x} este neutru")

# Exercitiul 4
if -2 < x < 13:
    print(f" Numarul {x} se afla in intervalul (-2,13)")
else:
    print(f"Numarul {x} nu se afla in intervalul (-2,13)")

# Exercitiul 5
y = int(input(f"Introdu inca un numar: "))
if (x - y) < 5:
    print(f"Diferenta dintre cele doua numere {x} si {y} este mai mica decat 5")
else:
    print(f"Diferenta dintre cele doua numere {x} si {y} nu este mai mica decat 5")

# Exercitiul 6
if not 5 < x < 27:
    print(f" Numarul {x} nu se afla in intervalul (5,27)")
else:
    print(f"Numarul {x} se afla in intervalul (5,27)")

#Exercitiul 7
x = int(x)
y = int(y)
if x==y:
    print(f" Numerele introduse sunt egale")
elif x>y:
    print(f"Numarul {x} este mai mare decat {y}")
else:
    print(f"Numarul {y} este mai mare decat {x}")

#Exercitiul 8
print(f"Introdu mai jos 3 numere aferente laturilor unui triunghi: ")
x = float(input(f"Prima latura este: "))
y = float(input(f"A doua latura este: "))
z = float(input(f"A treia latura este: "))
if x==y==z:
    print(f"Triunghiul cu laturile {x},{y},{z} este echilateral.")
elif x==y or x==z or y==z:
    print(f"Triunghiul cu laturile {x},{y},{z} este isoscel.")
else:
    print(f"Triunghiul cu laturile {x},{y},{z} este oarecare. ")

#Exercitiul 9
vocale = "a e i o u ă î â"
consoane = "q w r t y p s d f g h j k l z c v b n m ț ș"
litera = input(f"Introdu o litera: ")
if litera in vocale:
    print(f"Litera {litera} este vocala")
elif litera in consoane:
    print(f"Litera {litera} este consoana")
else:
    print(f"Caracterul introdus {litera} nu este o litera. Mai incearca! ")

#Exercitiul 10

nota = float(input(f"Introdu nota: "))
if 10 >= nota >= 9:
    print(f"Nota {nota} corespunde cu nota A")
elif 9 > nota >= 8:
    print(f"Nota {nota} corespunde cu nota B")
elif 8> nota >=7:
    print(f"Nota {nota} corespunde cu nota C")
elif 7> nota >=6:
    print(f"Nota {nota} corespunde cu nota D")
elif 6> nota >4:
    print(f"Nota {nota} corespunde cu nota E")
elif 4>= nota >= 1:
    print(f"Nota {nota} corespunde cu nota F")
else:
    print(f"Nota este invalida")

#Exercitii optionale
#Exercitiul 1
x = int(input(f"Introdu un nr format din 4 cifre: "))
if x > 999:
    print(f"Numarul {x} are minim 4 cifre")
else:
    print(f"Numarul {x} nu are minim 4 cifre")

#Exercitiul 2
if 99999 < x <1000000:
    print(f"Numarul {x} are fix 6 cifre")
elif x > 999999:
    print (f"Numarul {x} are mai mult decat 6 cifre")
else:
    print(f"Numarul {x} are mai putin decat 6 cifre")

#Exercitiul 3
if x%2 == 0:
    print(f"Numarul {x} este par")
else:
    print(f"Numarul {x} este impar")

#Exercitiul 4
x = int(input(f"Introdu un nr : "))
y = int(input(f"Introdu un nr : "))
z = int(input(f"Introdu un nr : "))
if x>y and x>z:
    print(f"Numarul {x} este cel mai mare")
elif y>x and y>z:
    print(f"Numarul {y} este cel mai mare")
else:
    print(f"Numarul {z} este cel mai mare")

#Exercitiul 5
print(f"Introdu mai jos unghiurile unui triunghi: ")
x = int(input(f"Introdu primul unghi al triunghiului : "))
y = int(input(f"Introdu al doilea unghi al triunghiului : "))
z = int(input(f"Introdu al treilea unghi al triunghiului : "))
if x+y+z == 180:
    print(f"Triunghiul cu unghiurile {x},{y} si {z} este valid")
else:
    print(f"Triunghiul este invalid")

#Exercitiul 6
expresie = 'Coral is either the stupidest animal or the smartest rock'
x = int(input(f"Introdu un nr: "))
lungimea_expresiei_fara_x = len(expresie)-x
print(expresie[0:lungimea_expresiei_fara_x])

#Exercitiul 7
print(expresie[0:5]+expresie[-5:])

#Exercitiul 8
index_cuv_rock = expresie.index('rock')
print(f"indexul primei litere a cuvantului rock este {index_cuv_rock}")
print(expresie[0:index_cuv_rock])

#Exercitiul 9
propozitie = input("Scrie o propozitie: ")
prima_litera = propozitie[0].lower()
ultima_litera = propozitie[-1].lower()
assert prima_litera==ultima_litera
print("Prima si ultima litera sunt la fel")

#Exercitiul 10
string_numere = "0123456789"
numar_par = string_numere[0:10:2]
numar_impar = string_numere[1:10:2]
print(f"Numerele pare sunt: {numar_par} si numerele impare sunt {numar_impar}" )
# Nu stiu cum am putea afla numerele dintr-un string dat de utilizator.

