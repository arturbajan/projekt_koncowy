import os


def menu():
    print('''
    0. test potrzebnych plików
    1. sprawdzi ile kobiet z danych przeżyło katastrofe
    2. sprawdzi ilu mężczyzn z danych przeżyło katastrofę
    3. policzy jaki procent osób ma uzupełnione dane o wieku
    4. wyświetli średnią wieku pasażerów, maksymalny wiek i minimalny wiek
    5 wyświetli podział procentowy na mężczyzn i kobiety.''')

    operacja_menu = int(input("Podaj numer operacji:\n"))


    if operacja_menu == 0:
        sciezki()
    elif operacja_menu == 1:
        pass
    elif operacja_menu == 2:
        pass
    elif operacja_menu == 3:
        pass
    elif operacja_menu == 4:
        pass
    elif operacja_menu == 5:
        pass
    else:
        print(f"Nie ma takiej operacji na: {operacja_menu}")
        menu()


def sciezki():
    pliki = ['/gender_submission.csv', '/test.csv', '/train.csv']
    for idx, pliki in enumerate(pliki, start=0):
        print(os.getcwd() + pliki,'=>',os.path.isfile(os.getcwd() + pliki))


def kobiety_zywe():
    pass


def mezczyzni_zywi():
    pass
