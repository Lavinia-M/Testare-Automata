import math


# Exercitiul 1
class Cerc:
    raza = 0
    culoare = ''

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Culoarea cercului este {self.culoare} si raza cercului este {self.raza}')

    def aria(self):
        return math.floor(math.pi * (self.raza ** 2))

    def diametru(self):
        return math.floor(self.raza * 2)

    def circumferinta(self):
        return math.floor(2 * self.raza * math.pi)


cerc_mov = Cerc(12, 'mov')
cerc_mov.descrie_cerc()
print(cerc_mov.aria())
print(cerc_mov.circumferinta())
print(cerc_mov.diametru())


# Exercitiul 2
class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = ''

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are culoarea {self.culoare}, are lungimea {self.lungime} si latimea {self.latime}')

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return 2 * (self.latime + self.lungime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
        print(noua_culoare)


dreptunghi_verde = Dreptunghi(12, 6, 'verde')

dreptunghi_verde.descrie()
print(dreptunghi_verde.aria())
print(dreptunghi_verde.perimetru())
dreptunghi_verde.schimba_culoarea("galben")
dreptunghi_verde.descrie()

# Exercitiul 3


class Angajat:
    nume = ''
    prenume = ''
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul cu numele {self.nume} si prenumele {self.prenume} are salariul {self.salariu}')

    def nume_complet(self):
        return self.nume+' '+self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        return self.salariu + ((self.salariu * procent)/100)


ioana = Angajat('Popescu', 'Ioana', 4000)
ioana.descrie()
print(ioana.nume_complet())
print(ioana.salariu_lunar())
print(ioana.salariu_anual())
print(ioana.marire_salariu(10))


# Exercitiul 4
class Cont:
    iban = ''
    titular_cont = ''
    sold = 0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        return self.sold - suma

    def creditare_cont(self, suma):
        return self.sold + suma


cont1 = Cont('RO31BTRLRONCRT123456', 'Popescu Ioana', 4000)
cont1.afisare_sold()
print(cont1.debitare_cont(200))
print(cont1.creditare_cont(4400))
