# Exercitiul 2
from abc import ABC


class FormaGeometrica(ABC):

    PI = 3.14

    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi.')


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self._latura = latura

    def getter_latura(self):
        print(f"Patratul are latura {self._latura}")
        return self._latura

    def setter_latura(self, latura_noua):
        print(f"Latura patratului era {self._latura}, iar acum este {latura_noua}. ")
        self._latura = latura_noua

    def deleter_latura(self):
        del self._latura

    def aria(self):
        return self._latura ** 2


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self._raza = raza

    def getter_raza(self):
        print(f'Raza cercului este {self._raza}.')

    def setter_raza(self, raza_noua):
        print(f"Raza cercului era {self._raza} si acum este {raza_noua}.")
        self._raza = raza_noua

    def deleter_raza(self):
        del self._raza

    def aria(self):
        return self._raza ** 2 * self.PI

    def descrie(self):
        print(f'Eu nu am colturi.')


patrat = Patrat(8)
patrat.descrie()
print(patrat.aria())
patrat.setter_latura(12)
patrat.getter_latura()
print(patrat.deleter_latura())

cerc = Cerc(5)
cerc.descrie()
print(cerc.aria())
cerc.getter_raza()
cerc.setter_raza(10)
print(cerc.deleter_raza())
