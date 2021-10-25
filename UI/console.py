from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import clasa_superioara_dupa_nume


def print_menu():
	print("1. Adauga rezervare.")
	print("2. Sterge rezervare.")
	print("3. Modifica rezervare.")
	print("4. Trece toate rezervarile facute pe un nume citit la o clasa superioara.")
	print("a. Afisare rezervari.")
	print("x. Iesire.")


def ui_adauga_rezervare(lista):
	id = input("Dati id-ul: ")
	nume = input("Dati numele: ")
	clasa = input("Dati clasa: ")
	pret = float(input("Dati pretul: "))
	checkin = input("Dati check-in-ul: ")
	return adauga_rezervare(id, nume, clasa, pret, checkin, lista)


def ui_sterge_rezervare(lista):
	id = input("Dati id-ul rezervarii de sters: ")
	return sterge_rezervare(id, lista)


def ui_modifica_rezervare(lista):
	id = input("Dati id-ul rezervarii de modificat: ")
	nume = input("Dati noul nume: ")
	clasa = input("Dati noua clasa: ")
	pret = float(input("Dati noul pret: "))
	checkin = input("Dati noul check-in: ")
	return modifica_rezervare(id, nume, clasa, pret, checkin, lista)


def ui_clasa_superioara_dupa_nume(lista):
	nume = input("Dati numele dupa care se va face modificarea: ")
	return clasa_superioara_dupa_nume(nume, lista)


def show_all(lista):
	for rezervare in lista:
		print(to_string(rezervare))


def run_menu(lista):
	while True:
		print_menu()
		optiune = input("Dati optiunea: ")
		if optiune == "1":
			lista = ui_adauga_rezervare(lista)
		elif optiune == "2":
			lista = ui_sterge_rezervare(lista)
		elif optiune == "3":
			lista = ui_modifica_rezervare(lista)
		elif optiune == "4":
			lista = ui_clasa_superioara_dupa_nume(lista)
		elif optiune == "a":
			show_all(lista)
		elif optiune == "x":
			break
		else:
			print("Optiune invalida!")
