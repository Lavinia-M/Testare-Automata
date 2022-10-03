import datetime
import time


# Exercitiul 1
def luna_an(x):
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        print(f'Luna introdusa de tine are 31 de zile.')
    elif x == 2:
        print(f'Luna introdusa de tine are 28 de zile.')
    else:
        print(f'Luna introdusa de tine are 30 de zile.')


print("Indicativ luna: Ian=1 , Feb=2, Martie=3,Apr=4,Mai=5,Iun=6,Iulie=7,Aug=8,Sept=9,Oct=10,Nov=11,Dec=12")
luna_introdusa_de_user = int(input("Nr aferent lunii pt care doresti sa afli numarul de zile este: "))
print(luna_an(luna_introdusa_de_user))

# Exercitiul 2
def calculator(x, y):
    return x + y, x - y, x * y, x / y


a, b, c, d = calculator(10,2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

# Exercitiul 3
def count_nr(lista_nr):
    dict_numere = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    numar = 0
    for i in range(0, 10):
        for numar in lista_nr:
            if numar == i:
                dict_numere[i] += 1
    return dict_numere

lista1 = [1, 3, 1, 5, 9, 7, 5, 5]
print(count_nr(lista1))


# Exercitiul 4
def max_nr(a, b, c):
    if a > b and a > c:
        print(f'{a} este cel mai mare numar dintre cele 3 introduse de tine.')
    elif b > a and b > c:
        print(f'{b} este cel mai mare numar dintre cele 3 introduse de tine.')
    else:
        print(f'{c} este cel mai mare numar dintre cele 3 introduse de tine.')


x = input(f"Introdu un numar: ")
y = input(f"Introdu al doilea numar: ")
z = input(f"Introdu al treilea numar: ")
print(max_nr(x, y, z))

# Exercitiul 5
def suma_numar(x):
    suma = 0
    for i in range(x+1):
        suma += i
    return suma


print(suma_numar(5))

print('******Bonus******')

# Ex 1
def intersectie_liste(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    l3 = l1 & l2
    return l3


lista1 = [1, 5, 69, 8, 25, 9, 58, 96, 87, 105, 65, 95]
lista2 = [5, 8, 6, 9, 4, 6, 69, 105, 58, 95]
print(f'Numerele comune din cele 2 liste sunt: {intersectie_liste(lista1,lista2)}')

# Exercitiul 2
def reducere_pret(pret, reducere):
    pret_redus = pret - (pret * reducere / 100)
    if 0 < reducere < 100:
        print(f'Pretul in urma reducerii aplicate este de: {pret_redus} lei')
    else:
        print(f' Reducerea nu se aplica. Valoarea reducerii nu este valida.')


print(reducere_pret(100, 10))
print(reducere_pret(100, 110))

# Exercitiul 3

def data_ora():
    t = time.asctime(time.localtime(time.time()))
    return t


print(data_ora())


# Exercitiul4

zi_nastere = datetime.date(2023,8,12)
data_curenta = datetime.date.today()


def calcul_nr_zile():
    zile_ramase = zi_nastere - data_curenta
    return zile_ramase


print(calcul_nr_zile())
