import random

# Exercitiul 1
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for nr in alte_numere:
    if nr % 2 == 0:
        numere_pare.append(nr)
    else:
        numere_impare.append(nr)
    if nr > 0:
        numere_pozitive.append(nr)
    else:
        numere_negative.append(nr)

print(f'Lista numerelor pare este {numere_pare}')
print(f'Lista numerelor impare este {numere_impare}')
print(f'Lista numerelor pozitive este {numere_pozitive}')
print(f'Lista numerelor negative este {numere_negative}')

# Exercitiul 2
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_sortate = alte_numere.copy()

for i in range(len(numere_sortate)):
    for j in range(len(numere_sortate) - 1):
        if numere_sortate[j] > numere_sortate[j + 1]:
            numere_sortate[j], numere_sortate[j + 1] = numere_sortate[j + 1], numere_sortate[j]

print(numere_sortate)

# Exercitiul 3


numar_ghicit = None
numar = random.randint(1, 30)
while numar_ghicit is None:
    numar_secret = int(input("Generati un numar random intre 1 si 30:  \n"))
    if numar_secret > numar:
        print('Nr secret e mai mic')
    elif numar_secret < numar:
        print('Nr secret e mai mare')
    else:
        print(f'Felicitari! Ai ghicit nr {numar_secret}!')
        break

# Exercitiul 4
nr_utilizator = int(input(f'Introdu un nr: '))
for i in range(1, nr_utilizator + 1):
    for j in range(0, i):
        print(i, end="")
    print("\n")

# Exercitiul 5

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for rand in tastatura_telefon:
    for element in rand:
        print(f'Numarul curent este {element}')
