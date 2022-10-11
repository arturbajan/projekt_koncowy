import os
import pandas as pd
from numpy import NaN


def menu():
    print('''
    0. test potrzebnych plików
    1. sprawdz ile kobiet z danych przeżyło katastrofe
    2. sprawdz ilu mężczyzn z danych przeżyło katastrofę
    3. policzy jaki procent osób ma uzupełnione dane o wieku
    4. wyświetli średnią wieku pasażerów, maksymalny wiek i minimalny wiek
    5. wyświetli podział procentowy na mężczyzn i kobiety.''')

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
        wiek_uzupelniony()

    elif operacja_menu == 4:
        oblicz()
        srednia_wieku()

    elif operacja_menu == 5:
        oblicz()
        pp_kobiet_do_menszczyzn()

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


def wiek_uzupelniony():
    npuste = analiza[analiza.Age > 0]
    snpuste = npuste['Age'].count()
    wsz = analiza['PassengerId'].count()
    pp =  round((snpuste/wsz)*100,2)
    print(f"Wszycy pasażerowie {wsz}  uzupełnione dane  {snpuste}  procent {pp}% ")

def srednia_wieku():
    sr = round(analiza['Age'].mean())
    wmin = analiza['Age'].min()
    wmax = analiza['Age'].max()
    print(f"Srednia wieku=>{sr}\nWiek minimialny=>{wmin}\nWiek maksymalny=>{wmax}")

def pp_kobiet_do_menszczyzn():
     kbt = analiza[analiza.Sex == 'female']  #/ analiza['PassengerId'].count()
     kbt_ = kbt['Sex'].count()
     print(kbt_)
