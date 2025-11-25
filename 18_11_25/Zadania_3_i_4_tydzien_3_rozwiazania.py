piwa: dict[str, tuple[float, float]] = {
    "Tyskie": (5.6, 4.5),
    "Żywiec Porter": (9.5, 4.0),
    "Lech": (5.2, 4.0),
    "Perła Chmielowa": (6.2, 3.8),
    "Warka Strong": (6.5, 5.5),
    "Żubr": (6.0, 4.0),
    "Romper": (7.0, 2.5),
    "Komes Porter": (9.0, 10.0),
    "Żywiec Białe": (5.0, 5.0),
    "Okocim Mocne": (7.0, 3.5),
    "Desperados": (5.9, 6.0),
    "Somersby": (4.5, 5.0),
    "Harnaś": (6.0, 3.0),
}


# Zadanie 3
# Chcemy znaleźć najtańszewgo browara ze słownika wszystkich browarów (piwa)
# W słowniku, kluczem jest nazwa piwa, a wartością kluczy jest krotka dwóch liczb zmiennoprzecinkowych
# Pierwsza liczba to stężenie procentowe browara, a druga to jego cena
# Tworzymy funkcję znajdz_najtanszy_najpotezniejszy_browar przyjmującą nasz słownik jako parametr
def znajdz_najtanszy_najpotezniejszy_browar(piwa: dict[str, tuple[float, float]]):
    # Definiujemy trzy puste listy do zapisywania w odpowiedniej kolejności znalezionych parametrów
    ceny: list = []
    procenty: list = []
    nazwy: list = []
    # Iterujemy po kluczach i ich wartościach w słowniku po kolei (metoda .items() na słowniku zwraca nam
    # krotkę (klucz, wartość)
    for nazwa, procenty_i_ceny in piwa.items():
        # Rozpakowujemy krotkę wartości (procentów i cen) na poszczególne zmienne adekwatnie do tego, czym są
        procent, cena = procenty_i_ceny
        # Sprawdzamy czy procent jest większy niż nasz zakładany próg stężenia alkoholu w browarze
        if procent >= 6:
            # Jeśli jest większy lub równy progowi, dodajemy zmienne do odpowiednich list w odpowiedniej kolejności
            ceny.append(cena)  # dodajemy cenę do list cen
            nazwy.append(nazwa)  # dodajemy nazwę do listy nazw
            procenty.append(procent)  # dodajemy procent do listy procentów
    # Chcemy znaleźć najtańszego browara, więc wyciągamy minimalną wartość ze WSZYSTKICH dodanych wartości browarów
    # o mocy większej niż zakładany próg
    minimalna_cena = min(ceny)
    # Dodawaliśmy parametry browarów w po kolei, więc indeks najtańszego browara w liście cen będzie też indeksem
    # jego nazwy w liście nazw i indeksem procentów w liście procentów
    indeks_ceny = ceny.index(minimalna_cena)
    # Wyświetlamy to co znaleźliśmy użytkownikowi odnosząc sie do odpowiednich list po znalezionym indeksie
    print(f"Najtańsze piwo to {nazwy[indeks_ceny]} o stężeniu alko {procenty[indeks_ceny]} za {ceny[indeks_ceny]} zł")


# KONIEC ZADANIA 3

# Zadanie 4
# Mamy nowo otwarty bar studencki i chcemy zjeść to co lubimy, musimy przeszukać menu i wybrać tylko to
# co nam się podoba. Menu jest w 2 słownikach dla napojów i jedzenia.
# A że jesteśmy studentami to bierzemy browca i kebsa.

# Słownik napojów ma w kluczach nazwe napoju, a w wartościach listy cech danego napoju
# tzn. gaz/niegaz, typ, %C2H5OH (alk)
napoje = {
    'Cola': ['gazowane', 'kofeina', '0'],
    'sok': ['niegazowane', 'owocowy', '0'],
    'Piwo1': ['gazowane', 'ciemne', '9'],
    'Piwo2': ['gazowane', 'jasne', '5']
}
# Słownik jedzenia ma w kluczach nazwy dań, a w wartościach listy różnych cech
jedzenie = {
    'Przysnacki': ['chrupkie', 'ostre', 'cebula'],
    'Lays': ['chrupkie', 'slone'],
    'Popcorn': ['maslo', 'slone'],
    'Kebab1': ['cebula', 'falafel', 'ostry sos'],
    'Kebab2': ['salata', 'frytki', 'mieso', 'ostry sos']
}


# Tworzymy funkcję przyjmującą w parametrach rodzaj piwa, procent alko, jakie dodatki kebsa chcemy,
# czego w kebsie nie chcemy
def znajdz_idealne_zamowienie(rodzaj_piwa, procent_alkoholu, dodatki_kebaba, zabronione_dodatki_kebaba):
    moje_piwa = []  # pusta lista do zapisywania wyników wyszukiwania dla piw
    # Dla każdej nazwy piwa i cech w menu z napojami
    for nazwa_piwa, cechy_piwa in napoje.items():
        # Jeśli rodzaj piwa jest w cechach i stężenie alko jest większe lub równe naszemu progowi zawartości alko
        if rodzaj_piwa in cechy_piwa and int(cechy_piwa[2]) >= procent_alkoholu:
            # Dodaj nazwe piwa do listy
            moje_piwa.append(nazwa_piwa)

    moje_danie = None  # Pusta zmienna dla dania
    # UWAGA
    # Konstrukty znajdujące się w funkcji all() to tak zwane KOMPREHENSJE
    # tłumacząc je w tym wypadku dla "dodatek in cechy_dania for dodatek in dodatki_kebaba":
    # porównanie "in" zwraca wartość boolean (True/False) zależnie czy dodatek zanjduje się w cechach
    # "for dodatek in dodatki_kebaba" to określenie zakresu, skąd ma zostać wybrany dodatek, w tym wypadku wybieramy
    # KAŻDY dodatek z listy dodatków od użytkownika
    # Ostatecznie możemy to porównać do listy prawd, np. [True, True, False] itp.
    # Funkcja all() przyjmująca tą listę zwróci True tylko wtedy, gdy wszystkie elementy w liście to True
    # W przeciwnym wypadku zwraca False.

    # Dla hażdego dania i cech danai w menu z szamą
    for nazwa_dania, cechy_dania in jedzenie.items():
        # jeśli WSZYSTKIE dodatki z listy dodatków podanych przez użytkownika są w daniu
        # ORAZ WSZYSTKIE niechciane dodatki NIE znajdują się w cechach dania
        if all(dodatek in cechy_dania for dodatek in dodatki_kebaba) and all(
                zabroniony_dodatek not in cechy_dania for zabroniony_dodatek in zabronione_dodatki_kebaba):
            # przypisz nazwę dania dla
            moje_danie = nazwa_dania

    # Zwracamy listę piw i wybrane danie
    return moje_piwa, moje_danie


# Wykonamy zadanie
def wykonaj_zadanie_4():
    # Pobierz preferencje od użytkownika
    rodzaj_piwa = input("Jaki rodzaj piwa preferujesz? (np. ciemne, jasne): ")
    procent_alkoholu = int(input("Podaj minimalny procent alkoholu: "))
    dodatki_kebaba = input("Jakie dodatki chcesz w kebabie? (np. ostry sos, mieso): ").split(', ')
    zabronione_dodatki_kebaba = input("Jakie dodatki nie chcesz w kebabie? (np. cebula, falafel): ").split(', ')
    print(f'{rodzaj_piwa=}\n{procent_alkoholu=}\n{dodatki_kebaba=}\n{zabronione_dodatki_kebaba=}')

    # Znajdź idealne zamowienie
    moje_piwa, moj_kebab = znajdz_idealne_zamowienie(rodzaj_piwa, procent_alkoholu, dodatki_kebaba,
                                                     zabronione_dodatki_kebaba)

    # Wyświetl wyniki
    print("Moje ulubione piwa to:", moje_piwa)
    print("A do tego zamówię:", moj_kebab)


if __name__ == "__main__":
    znajdz_najtanszy_najpotezniejszy_browar(piwa)
    wykonaj_zadanie_4()
