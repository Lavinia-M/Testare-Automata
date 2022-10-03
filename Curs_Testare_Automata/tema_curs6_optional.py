import datetime

# Exercitiul 1


class Factura:
    seria = 'IT'
    numar = 0
    nume_produs = ''
    cantitate = 0
    pret_buc = 0

    def __init__(self, numar, nume_produs, cantitate, pret_bucata):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_bucata

    def schimba_cantitatea(self, noua_cantitate):
        self.cantitate = noua_cantitate

    def schimba_pretul(self, noul_pret):
        self.pret_buc = noul_pret

    def schimba_nume_produs(self, noul_nume):
        self.nume_produs = noul_nume

    def total_factura(self):
        return self.pret_buc * self.cantitate


factura1 = Factura(1, 'Telefon', 7, 700)
print(f'Factura seria {factura1.seria} numar {factura1.numar}')
print(f'Data: {datetime.datetime.today()}')
print('Produs | Cantitate| Pret bucata | Total')
print(f'{factura1.nume_produs}| {factura1.cantitate}        |{factura1.pret_buc}          |{factura1.total_factura()}')

print(50*'*')
factura1.schimba_nume_produs('Smartphone')
factura1.schimba_cantitatea(5)
factura1.schimba_pretul(1000)
# Verificare
print(f'Factura seria {factura1.seria} numar {factura1.numar}')
print(f'Data: {datetime.datetime.today()}')
print('Produs | Cantitate| Pret bucata | Total')
print(f'{factura1.nume_produs}| {factura1.cantitate}        |{factura1.pret_buc}          |{factura1.total_factura()}')

# Exercitiul2


class Masina:
    marca = 'VW'
    model = ''
    viteza_maxima = 0
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'negru', 'galben', 'rosu', 'verde', 'albastru', 'maro', 'portocaliu'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Masina {self.marca}, model {self.model}, de culoare {self.culoare},are viteza maxima de '
              f'rulare de {self.viteza_maxima} km/h.')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare_noua):
        if culoare_noua in self.culori_disponibile:
            self.culoare = culoare_noua
            print(f'Culoarea {culoare_noua} aleasa de dvs este dispobinila')
        else:
            print(f'Culoarea aleasa nu este dispobinila')

    def accelereaza(self, viteza):
        if viteza > self.viteza_maxima:
            self.viteza_actuala += viteza
            print(f'Am accelerat pana la viteza maxima de {self.viteza_maxima} km/h.')
        else:
            if viteza < 0:
                print(f'Eroare!!!')
            else:
                self.viteza_actuala += viteza
                print(f'Am accelerat cu {viteza} km/h si am ajuns la viteza de {self.viteza_actuala} km/h.')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Masina franeaza. Am ajuns la viteza de {self.viteza_actuala} km/h.')


masina1 = Masina('tiguan', 260)
masina1.descrie()
masina1.accelereaza(-5)
masina1.accelereaza(20)
masina1.accelereaza(300)
masina1.franeaza()
masina1.vopseste("mov")
masina1.vopseste("albastru")
masina1.vopseste("rosu")
