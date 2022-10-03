#Exercitiul 1
masini = ['Audi','Volvo','BMW','Mercedes','Aston Martin', 'Lastun', 'Fiat','Trabant','Opel']

for masina_preferata in masini:
    print(f'Masina mea preferata este {masina_preferata}')
print("-"*100)
for index in range(len(masini)):
    print(f'Masina mea preferata este {masini[index]}')
print("-"*100)

i = 0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i += 1
print("-"*100)

#Exercitiul 2
for index in range(1,len(masini)-1):
    print(f'Masina mea preferata este {masini[index].upper()}')
else:
    print(masini)

#Exercitiul 3
masina_dorita = input(f'Introdu numele masinii dorite: ' )
for masina in masini:
    if masina == masina_dorita:
        print(f'Am gasit masina dorita de dvs.')
        break
    else:
        print(f'Nu am gasit masina {masina_dorita}.Mai cautam.')
else:
    print(f'Aceasta marca de masina nu se regaseste in lista.')

#Exercitiul 4
for masina_prezentata in masini:
    if masina_prezentata == "Lastun" or masina_prezentata == "Trabant":
        continue
    print(f'S-ar putea sa va placa masina {masina_prezentata}.')

#Exercitiul 5
masini_vechi = []
for masina in masini:
    if masina == "Lastun" :
        masini_vechi.append(masina)
        masini.remove("Lastun")
        masini.append("Tesla")
    elif masina == "Trabant":
        masini_vechi.append(masina)
        masini.remove("Trabant")
        masini.append("Tesla")
        print(f'Modele vechi: {masini_vechi}')
        print(f'Modele noi: {masini}')

#Exercitiul 6
# pret_masini ={'Dacia':6800,'Lastun':500,'Opel':1100,'Audi':19000,'BMW':23000}
# buget_client = 15000
#
# for masina_in_buget in pret_masini:
#
# print(f'Masina care se incadreaza in buget este: {pret_masini.keys()}')

#Exercitiul 7
numere = [5,7,3,9,3,3,1,0,-4,3]
numar = 0
for i in numere:
    if i == 3:
        numar += 1
print(f'Numarul 3 apare de {numar} ori')

# Exercitiul 8
numere = [5,7,3,9,3,3,1,0,-4,3]
suma_numere = 0
for nr in numere:
     suma_numere += nr
print(f'Suma numerelor din lista este: {suma_numere}')

#Exercitiul 9
numere = [5,7,3,9,3,3,1,0,-4,3]
nr_maxim = 0
for n in numere:
    if n > nr_maxim:
        nr_maxim = n
print(f'Cel mai mare nr este {nr_maxim}')


# for nr_mare in numere:
#     numere.sort()
#     nr_mare +=1
# print(f'Cel mai mare numar este {numere[-1]}')

#Exercitiul 10
for nr_mare in numere:
    numere.sort()
    nr_mare +=1
    if nr_mare>0:
        nr_mare = -1* numere[-1]
print (f'Valoarea negativa a celui mai mare numar din lista este {nr_mare}')
numere[-1]=nr_mare
print(f'Noua lista de numere: {numere}')
















