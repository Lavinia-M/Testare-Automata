""" Exercitiul 2
   O variabila de tip String reprezinta un sir de caractere ce poate contine cifre, litere sau expresii delimitate
      prin ghilimele simple.
"""

""" Exercitiul 4
  definim si initializam variabilele string, integer, boolean si float
  """


class Tema1:
    categorie = 'tableta'
    brand = 'Iphone'
    an_lansare = 2022
    card_memorie = False
    pret = 4999.99

    # Printam mesaj in consola
    print(f'Prezentare caracteristici pentru noul model de : {categorie} {brand}'),
    print(f'Anul lansarii produsului este in: {an_lansare}'),
    print(f'Se poate insera card de memorie: {card_memorie}'),
    print(f'Pretul produsului este de : {pret} lei')

    # Exercitiul 6
    for i in range(1, 20, 3):
        print(i)

    ''' Am printat rezultatul functiei de mai sus,
  rezultand o crestere din 3 in 3 a valorii i, incepand cu 1 pana la maxim 20.'''
