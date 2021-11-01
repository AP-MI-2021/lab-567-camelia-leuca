from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from UI.console import show_all


def meniu_comanda():
    print("Adauga rezervare : add, id, nume, clasa, pret, chekc-in")
    print("Sterge o rezervare: delete, id")
    print("Modifica o rezervare: update, id, nume, clasa, pret,check-in")
    print("Afisare rezervari: showall")
    print("Iesire: stop")


def comanda_meniu(lista):
    while True:
        string = input()
        if string == "help":
            meniu_comanda()
        elif string == "showall":
            show_all(lista)
        elif string == "stop":
            break
        else:
            comenzi = string.split(";")
            for elemente in comenzi:
                comanda = elemente.split(",")
                if comanda[0] == "add":
                    try:
                        comanda[4] = int(comanda[4])
                        lista = adauga_rezervare(comanda[1], comanda[2], comanda[3], comanda[4], comanda[5], lista)
                    except ValueError as ve:
                        print("Eroare {}".format(ve))
                elif comanda[0] == "delete":
                    try:
                        lista = sterge_rezervare(comanda[1], lista)
                    except ValueError as ve:
                        print("Eroare {}".format(ve))
                elif comanda[0] == "update":
                    try:
                        comanda[4] = int(comanda[4])
                        lista = modifica_rezervare(comanda[1], comanda[2], comanda[3], comanda[4], comanda[5], lista)
                    except ValueError as ve:
                        print("Eroare {}".format(ve))
                else:
                    print("Comanda gresita!")
