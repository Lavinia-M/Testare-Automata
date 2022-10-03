import math

# Exercitiul 1
def suma_a_2numere(nr1, nr2):
    return nr1 + nr2


a = int(input("Introdu primul nr: "))
b = int(input("Introdu al doilea nr: "))
print(f'Suma celor doua numere {a} si {b} este {suma_a_2numere(a, b)}')

# Exercitiul 2
def nr_par(nr):
    if nr % 2 == 0:
        return True
    else:
        return False


a = int(input("Introdu un nr: "))
print(nr_par(a))

# Exercitiul 3
def suma_caractere_nume_complet(nume, prenume1, prenume2):
    return len(nume)+len(prenume1)+len(prenume2)


nume = input("Introdu numele tau : \n")
prenume = input("Introdu prenumele tau : \n")
prenume_mijlociu = input("Introdu al doilea prenume : \n")

print(f'Nr total de caractere aferent numelui tau este de: '
      f'{suma_caractere_nume_complet(nume, prenume, prenume_mijlociu)}')

# Exercitiul 4
def arie_dreptunghi(lungime, latime):
    return lungime * latime


lungimea = int(input("Introdu lungimea dreptunghiului:"))
latimea = int(input("Introdu latimea dreptunghiului:"))
print(f'Aria dreptunghiului este {arie_dreptunghi(lungimea, latimea)}')

# Exercitiul 5

def arie_cerc(raza):
    return math.pi * (raza**2)


lungime_raza_cerc = int(input("Introdu lungimea raza cercului:"))
print(f'Aria cercului este {arie_cerc(lungime_raza_cerc)}')

# Exercitiul 6
def caracter_de_gasit(lit):
    expresie = 'Bine ai venit in echipa IT Factory!'
    if lit in expresie[::1]:
        return True
    else:
        return False


litera = input("Introdu o litera : \n")
print(caracter_de_gasit(litera))

# Exercitiul 7
def calculator_litere_mari_si_mici(expresie):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in expresie:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print(f'Propozitia dvs este:', expresie)
    print(f'Nr de caractere lower case este:', d["LOWER_CASE"])
    print(f'Nr de caractere upper case este:', d["UPPER_CASE"])


calculator_litere_mari_si_mici('Bine ai venit in echipa IT Factory')


# Exercitiul 8
def numere_pozitive(lista_numere):
    lista_nr_pozitive = []
    for i in lista_numere[::1]:
        if i > 0:
            lista_nr_pozitive.append(i)
            i += 1
    return lista_nr_pozitive


lista = [-4, 5, -6, -8, 9, 12, 15, -3]
print(f'Lista numerelor pozitive din lista {lista} este: {numere_pozitive(lista)}')

# Exercitiul 9
def cel_mai_mare_nr(a, b):
    if a > b:
        print(f'{a} este mai mare decat {b}')
    elif b > a:
        print(f'{b} este mai mare decat {a}')
    else:
        print(f'Numerele sunt egale')


x = int(input(f'Introdu nr: '))
y = int(input(f'Introdu nr: '))
print(cel_mai_mare_nr(x, y))
cel_mai_mare_nr(5, 10)

# Exercitiul 10
def nr_nou_in_set(numar, set_nr):
    if numar in set_nr:
        print(f'Nu am adaugat nr {numar} in set.Acesta exista deja.')
        return False
    else:
        print(f'Am adaugat nr {numar} in set.')
        return True


set_numere = {1, 3, 7, 9}
nr_nou_in_set(5, set_numere)
