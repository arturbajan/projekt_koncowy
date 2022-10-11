import os
import pandas as pd


def menu():
    print('''
    0. test potrzebnych plików
    1. sprawdz ile kobiet z danych przeżyło katastrofe
    2. sprawdz ilu mężczyzn z danych przeżyło katastrofę
    3. policzy jaki procent osób ma uzupełnione dane o wieku
    4. wyświetli średnią wieku pasażerów, maksymalny wiek i minimalny wiek
    5 wyświetli podział procentowy na mężczyzn i kobiety.''')

    operacja_menu = int(input("Podaj numer operacji:\n"))

    if operacja_menu == 0:
        sciezki()
        menu()
    elif operacja_menu == 1:
        oblicz()
        kobiety_zywe()

    elif operacja_menu == 2:
        oblicz()
        mezczyzni_zywi()

    elif operacja_menu == 3:
        oblicz()
    elif operacja_menu == 4:
        oblicz()
    elif operacja_menu == 5:
        oblicz()
    else:
        print(f"Nie ma takiej operacji na: {operacja_menu}")
        menu()


def sciezki():
    pliki = ['/gender_submission.csv', '/test.csv', '/train.csv']
    for idx, pliki in enumerate(pliki, start=0):
        print(os.getcwd() + pliki, '=>', os.path.isfile(os.getcwd() + pliki))
    wdf()
def oblicz():
    wdf()


def wdf():
    df = pd.read_csv(os.getcwd() + '/train.csv')
    return df


analiza = wdf()


def kobiety_zywe():
    kz = analiza[(analiza.Sex == 'female') & (analiza.Survived == 1)]
    sumak = kz['Survived'].sum()
    print(f'sprawdz ile kobiet z danych przeżyło katastrofe {sumak}')


def mezczyzni_zywi():
    mz = analiza[(analiza.Sex == 'male') & (analiza.Survived == 1)]
    sumam = mz['Survived'].sum()
    print(f'sprawdz ilu mężczyzn z danych przeżyło katastrofę {sumam}')
