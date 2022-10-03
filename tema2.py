""" Exercitiul 1 - O variabila este zona din memorie a unui calculator care tine date. O variabila poate fi denumita
oricum, evitand  cuvintele cu semnificatie specifice asemanatoare functiilor, sintaxelor.
 """
# Exercitiul 2
nume_prenume_copil= "Popescu Andrei"
varsta = 5
greutate = 20.7
reinscris = True
print(greutate)

#Exercitiul 3
print(type(nume_prenume_copil))
print(type(varsta))
print(type(greutate))
print(type(reinscris))

#Exercitiul 4
greutate = round(greutate)
print(greutate)
print(type(greutate))

#Exercitiul 5
greutate= float(greutate)
print(f'Numele si prenumele copilului este: {nume_prenume_copil}')
print(f'Varsta copilului la inceputul anului este: {varsta} ani')
print(f'Greutatea copilului este de : {greutate} kg')
print(f'Copilul este reinscris: {reinscris}')
print(type(greutate))
#In urma rotunjirii, variabila greutate a devenit integer, iar acum am schimbat-o la tipul care a fost anterior- float.

#Exercitiul 6
nume= input("Numele tau este:")
prenume1= input("Primul tau prenume este:")
prenume2= input("Al doilea tau prenume este:")
nr_caractere= len(nume)+len(prenume1)+len(prenume2)
print(f"Numele complet are {nr_caractere} caractere")

#Exercitiul 7
lungimea = int(input("Introdu lungimea dreptunghiului:"))
latimea =  int(input("Introdu latimea dreptunghiului:"))
aria = lungimea*latimea
print(f'Aria dreptunghiului este {aria}')

#Exercitiul 8
afirmatie = "Coral is either the stupidest animal or the smartest rock:"
numara = " the "
de_cate_ori = afirmatie.count(numara)
print(f" Cuvantul 'the' apare de {de_cate_ori} ori")
# Daca punem variabila numara fara spatii putem afla de cate ori apare grupul "the" din interiorul cuvintelor.

#Exercitiul 9
afirmatie = "Coral is either the stupidest animal or the smartest rock:"
numara1 = "the"
de_cate_ori1 = afirmatie.count(numara1)
print(f" Grupul de cuvinte 'the' apare de {de_cate_ori1} ori")

#Exercitiul 10
# verificare = isinstance(afirmatie,int)
#
# assert verificare == True
# print("Afirmatia contine doar numere")


#-------------EXERCITII OPTIONALE --------------------------------------------------------------------

cuvant = input(f"Scrie un cuvant: ")
mijloc = cuvant[(len(cuvant)-1)//2:(len(cuvant)+2)//2]
print(f"Litera din mijlocul cuvantului este: {mijloc}")

#Exercitiul 2
# assert cuvant == cuvant[::-1]
# print(f"palindrom")

#Exercitiul 3
expresie = str(input("Scrie doua cuvinte:").split())
print(expresie )

#Exercitiul 4
expresie = str(input("Scrie doua cuvinte:"))
primul_caracter = expresie[0]
print(f"Primul caracter este: {primul_caracter}")

ultimul_caracter = int(expresie.rindex(primul_caracter))
alte_caractere = expresie[ultimul_caracter:len(expresie)]
expresie = expresie [1:ultimul_caracter].replace(primul_caracter,primul_caracter.upper())
expresie_cu_upper = primul_caracter + expresie + alte_caractere
print(expresie_cu_upper)



#Exercitiul 5
utilizator= input("Introdu numele de utilizator:")
parola = input("Introdu parola:")
nrcaractere = len(parola)
ascunde_parola = nrcaractere * '*'
print(f" Parola pt user este {ascunde_parola} si are {nrcaractere} caractere")

