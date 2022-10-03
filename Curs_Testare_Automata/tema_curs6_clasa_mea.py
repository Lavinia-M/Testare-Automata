import datetime
import math


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

    def poprire_cont(self):
        # se aplica poprire pe cont doar daca veniturile depasesc valoarea de 2500 lei, alfel nu se aplica poprire.
        suma_poprire = math.floor(0.25 * self.sold)
        if self.sold > 2500:
            self.sold = self.sold - suma_poprire
            print(f'Soldul dupa aplicarea popririi pe cont este {self.sold} lei,'
                  f' iar poprirea este in valoare de {suma_poprire} lei.')
        else:
            print(f'Nu se poate pune poprire pe cont,venituri insuficiente.')

    def rata_lunara(self, suma_plata):
        # Clientul are o rata lunara de platit, la data scadenta de 15.
        # Aici nu am stiut cum sa definesc doar ziua de 15 a lunii curente,de aceea am trecut predefinit 15 Sept 2022.
        zi_plata = datetime.date(2022, 9, 15)
        if datetime.date.today() > zi_plata:
            self.sold = self.sold - suma_plata
            print(f'S-a efectuat rata lunara in valoare de {suma_plata} lei.')
        elif datetime.date.today() == zi_plata:
            print(f'Astazi se va efectua plata pentru rata lunara in valoare de {suma_plata} lei.')
        else:
            print(f'Mai aveti {zi_plata-datetime.date.today()} zile pana la efectuarea platii. ')


cont1 = Cont('RO31BTRLRONCRT123456', 'Popescu Ioana', 2000)
cont1.afisare_sold()
cont1.poprire_cont()
cont1.rata_lunara(500)
cont1.afisare_sold()  # Verificare pt a vedea cat a ramas soldul titularului dupa platile efectuate.

print(80*'-')
cont2 = Cont('RO24BRDE24945825252', 'Georgescu Dan', 5000)
cont2.afisare_sold()
cont2.poprire_cont()
cont2.rata_lunara(700)
cont2.afisare_sold()
print(80*'-')

cont3 = Cont('RO31BTRLRONCRT456982564', 'Ion Andrei', 10000)
cont3.afisare_sold()
cont3.poprire_cont()
cont3.rata_lunara(1500)
cont3.afisare_sold()
