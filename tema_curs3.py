#Exercitiul 1
note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
note_muzicale= note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

#Exercitiul 2
numara_do = "do"
print(note_muzicale.count(numara_do))

#Exercitiul 3
lista1 = [3,1,0,2]
lista2 = [6,5,4]
print(lista1 + lista2)
lista_complexa = lista1.extend(lista2)
print(lista_complexa)

#Exercitiul 4
lista_complexa.sort()
print(lista_complexa)
lista_complexa.remove(0)
print(lista_complexa)

#Exercitiul 5
if len(lista_complexa) == 0:
    print(f"Lista este goala")
else:
    print("Lista nu este goala")

#Exercitiul 6
lista_complexa.clear()
print(lista_complexa)

#Exercitiul 7
if len(lista_complexa) == 0:
    print(f"Lista este goala")
else:
    print("Lista nu este goala")

#Exercitiul 8
dict1 = {'Ana':8,'Gigel':10,'Dorel':5}
print(dict1.keys())

#Exercitiul 9
print('Ana a luat nota ' + str(dict1['Ana']))
print('Gigel a luat nota ' + str(dict1['Gigel']))
print('Dorel a luat nota ' + str(dict1['Dorel']))

#Exercitiul 10
dict1.update({'Dorel':6})
print(dict1)

#Exercitiul 11
dict1.__delitem__('Gigel')
print(dict1)
dict1.update({'Ionica':9})
print(dict1)

#Exercitiul 12
zile_sapt = {'luni','marti','miercuri','joi','vineri','sambata','duminica'}
weekend = {'sambata','duminica'}
zile_sapt.add('luni')
print(zile_sapt)  #In set nu se afiseaza atribute duplicate,ori de cate ori le adaugam se afiseaza doar o data.

#Exercitiul 13
if weekend.issubset(zile_sapt):
    print(f"Weekend este subset al zilelor saptamanii")
else:
    print(f"Weekend nu este subset al zilelor saptamanii")

#Exercitiul 14
print(zile_sapt.difference(weekend))

#Exercitiul 15
print(zile_sapt.intersection(weekend))

