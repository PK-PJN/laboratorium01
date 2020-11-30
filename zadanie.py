#!/usr/bin/python3

"""Przetwarzanie języka naturalnego, laboratorium 1."""

import collections
import functools

import morfeusz2
import matplotlib.pyplot as plt


KSIĄŻKA = ''  # TU(3): wpisać nazwę pliku z tekstem książki.

# Chociaż biblioteki morfeusz2 używa się zwykle do analizowania
# dłuższych tekstów, my używamy jej tylko do analizowania
# pojedynczych wyrazów.
# Dzięki parametrowi praet='composite' formy czasu przeszłego
# i trybu przypuszczającego są analizowane jako jeden segment,
# a nie jako np. 'robił' + 'by' + 'm'.
MORFEUSZ = morfeusz2.Morfeusz(praet='composite')


def podaj_wyrazy(nazwa_pliku):
    # TU(4): uzupełnić zgodnie z instrukcją.


def wypisz_skrajne_znaki_wyrazów(nazwa_pliku):
    # TU(4): uzupełnić zgodnie z instrukcją.


@functools.lru_cache(maxsize=None)
def formy_podstawowe(wyraz):
    formy = []
    for interpretacja in MORFEUSZ.analyse(wyraz):
        formy.append(interpretacja[2][1])
    return sorted(formy)


def jednoznaczna_forma_podstawowa(wyraz):
    formy = formy_podstawowe(wyraz)
    # TU(7): uzupełnić zgodnie z instrukcją.


def main():
    wypisz_skrajne_znaki_wyrazów(KSIĄŻKA)
    return
    # TU(5): zakomentować dwa powyższe wiersze.
    # TU(5): zaprogramować zliczanie wystąpień poszczególnych
    # wyrazów w kolekcji `wyrazy` typu `collections.Counter`
    # oraz zliczanie sumarycznej liczby wyrazów w zmiennej
    # `długość_tekstu` typu liczbowego.
    # TU(5): wypisać 10 najczęstszych wyrazów i ich częstość.

    plt.xscale('log')
    plt.yscale('log')
    # Rysujemy podwójnie logarytmiczny wykres częstości
    # wystąpień wyrazów, od najczęstszego do najrzadszych.
    y = []
    for _, ile_wystąpień in wyrazy.most_common():
        y.append(ile_wystąpień / długość_tekstu)
    plt.plot(y)
    plt.title(f'Częstość wystąpień {len(wyrazy)} wyrazów\nw książce {KSIĄŻKA}')
    plt.show()
    return
    # TU(6): skasować powyższy wiersz.

    plt.xscale('log')
    plt.yscale('linear')
    y = []
    # TU(6): narysować półlogarytmiczny wykres pokrycia tekstu
    # przez wyrazy. N-ty element tablicy `y` ma być równy sumie
    # częstości wyrazów od najczęstszego do N-tego pod względem
    # malejącej częstości.
    plt.title(f'Pokrycie tekstu przez {len(wyrazy)} wyrazów\nw książce {KSIĄŻKA}')
    plt.show()

    # TU(8): zaprogramować zliczanie wystąpień form podstawowych
    # wyrazów w kolekcji `formy` typu `collections.Counter`
    # i rysowanie wykresów częstości ich wystąpień oraz pokrycia
    # przez nie tekstu.
    plt.title(f'Częstość wystąpień {len(formy)} form podstawowych\nw książce {KSIĄŻKA}')
    plt.title(f'Pokrycie tekstu przez {len(formy)} form podstawowych\nw książce {KSIĄŻKA}')


if __name__ == '__main__':
    main()
