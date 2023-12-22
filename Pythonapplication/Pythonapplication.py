import random
from random import randint

wybranyplan = {
    "Kraj": "Nie wybrano zadnego kranju",
    "Ilosc dni": 0,
    "Cena": 0,
}

wszystkieoferty = set()

listawycieczek = ['Egipt', 'Turcja', 'Grecja', 'Malediwy', 'Japonia', 'Indonezja', 'Australia']

class Trip:
 wycieczka = ''
 dni = 0
 cena = 0
 def __init__(self, wycieczka, iloscdni, cena):
    self.wycieczka = wycieczka
    self.dni = iloscdni
    self.cena = cena

def funkcja_losowa(x, y, z):
    while True:
        x = random.choice(listawycieczek)
        y = randint(3,30)
        z = randint(3000, 10000)
        print("Oto wygenerowana propozycja:")
        print(x)
        print('liczba dni: ', end='')
        print(y) 
        print('cena za osobe: ', end='')
        print(z)
        pytanie = int(input("Czy Wymieniona wyzej oferta cie interesuje? \n 1 - TAK, powrot do menu \n2 - NIE, powrot do menu \n Pozostale znaki - losuj ponownie\n"))
        if pytanie == 1:
            print("wybrano oferte podrozy")
            wybranyplan.update({"Kraj": x})
            wybranyplan.update({"Ilosc dni": y})
            wybranyplan.update({"Cena": z})
            break
        if pytanie == 2:
            print("powracam do menu")
            break
        else:
            print("losuje ponownie")

def funkcja_wyboru(x, y, z):
    print("Wybierz interesujacy cie kraj sposrod listy najchetniej odwiedzanych krajow: ")
    print(listawycieczek)
    while True:
        x = input("Wpisz nazwe kraju ktory cie interesuje: ")
        if x in listawycieczek:
            print("Poprawnie wybrano kraj")
            y = int(input("Wpisz interesujaca cie dlugosc pobytu od 3 do 30 dni: "))
            if 3 <= y <= 30:
                print("Poprawnie wybrano ilosc dni")
                z = int(input("Wpisz interesujaca cie cene wycieczki (najtansze zaczynaja sie od 3000): "))
                if z >= 3000:
                    print("Wybrano poprawna cene. Zapisuje wybrana oferte")
                    wybranyplan.update({"Kraj": x})
                    wybranyplan.update({"Ilosc dni": y})
                    wybranyplan.update({"Cena": z})
                    wycieczka = Trip(x, y,z)
                    wszystkieoferty.add(wycieczka)
                    break
                else:
                    print("zbyt niska cena")
                    break
            else:
                print("Zbyt mala\duza ilosc")
                break
        else:
            print("Nie ma takiego kraju na liscie dostepnych krajow")
            break

while True:
    print('Witaj w biurze podrozy. Wybierz opcje, ktora chcesz wykonac: ')
    print('1 - Wyszukaj oferte podrozy wedlug preferencji')
    print('2 - wylosuj proponowana oferte podrozy')
    print('3 - pokaz wybrane oferty')
    print('0 - wyjdz z biura podrozy')

    wybor = int(input("Wpisz numer opcji: "))

    match wybor:

        case 1:
            funkcja_wyboru(Trip.wycieczka,Trip.dni, Trip.cena)

        case 2:
           wycieczka = ''
           iloscdnirandom = 0
           cenarandom = 0
           funkcja_losowa(wycieczka, iloscdnirandom, cenarandom)

        case 3:
            for i in wszystkieoferty:
                print(i.wycieczka)
    
        case 0:
            print('Pomyslnie opuszczono biuro podrozy')
            break

        case _:
            print("wpisano niepoprawny symbol") 