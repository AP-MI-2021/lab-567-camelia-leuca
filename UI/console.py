from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionalitati import clasa_superioara_dupa_nume, ieftinire_checkin, pret_maxim_fiecare_clasa, \
	ordonare_pret_descrescator, sume_preturi_fiecare_nume


def print_menu():
	print("1. Adauga rezervare.")
	print("2. Sterge rezervare.")
	print("3. Modifica rezervare.")
	print("4. Trece toate rezervarile facute pe un nume citit la o clasa superioara.")
	print("5. Reduce pretul tuturor rezervarilor la care s-a facut check-in cu un procentaj citit.")
	print("6. Determina pretul maxim pentru fiecare clasa.")
	print("7. Ordoneaza rezervarile descrescator dupa pret.")
	print("8. Afiseaza sumele preturilor pentru fiecare nume.")
	print("a. Afisare rezervari.")
	print("x. Iesire.")


def ui_adauga_rezervare(lista):
	try:
		id = input("Dati id-ul: ")
		nume = input("Dati numele: ")
		clasa = input("Dati clasa: ")
		pret = float(input("Dati pretul: "))
		checkin = input("Dati check-in-ul: ")
		return adauga_rezervare(id, nume, clasa, pret, checkin, lista)
	except ValueError as ve:
		print("Eroare {}".format(ve))
		return lista


def ui_sterge_rezervare(lista):
	try:
		id = input("Dati id-ul rezervarii de sters: ")
		return sterge_rezervare(id, lista)
	except ValueError as ve:
		print("Eroare {}".format(ve))
		return lista


def ui_modifica_rezervare(lista):
	try:
		id = input("Dati id-ul rezervarii de modificat: ")
		nume = input("Dati noul nume: ")
		clasa = input("Dati noua clasa: ")
		pret = float(input("Dati noul pret: "))
		checkin = input("Dati noul check-in: ")
		return modifica_rezervare(id, nume, clasa, pret, checkin, lista)
	except ValueError as ve:
		print("Eroare {}".format(ve))
		return lista


def ui_clasa_superioara_dupa_nume(lista):
	nume = input("Dati numele dupa care se va face modificarea: ")
	return clasa_superioara_dupa_nume(nume, lista)


def ui_ieftinire_checkin(lista):
	try:
		procent = float(input("Dati procentajul cu care se vor ieftini rezervarile: "))
		return ieftinire_checkin(lista, procent)
	except ValueError as ve:
		print("Eroare {}".format(ve))
		return lista


def ui_pret_maxim_fiecare_clasa(lista):
	rezultat = pret_maxim_fiecare_clasa(lista)
	for clasa in rezultat:
		print("Clasa {} are pretul maxim {}.".format(clasa, rezultat[clasa]))


def ui_ordonare_pret_descrescator(lista):
	show_all(ordonare_pret_descrescator(lista))


def ui_sume_preturi_fiecare_nume(lista):
	rezultat = sume_preturi_fiecare_nume(lista)
	for nume in rezultat:
		print("Pentru numele {} suma este {}".format(nume, rezultat[nume]))


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
		elif optiune == "5":
			lista = ui_ieftinire_checkin(lista)
		elif optiune == "6":
			ui_pret_maxim_fiecare_clasa(lista)
		elif optiune == "7":
			ui_ordonare_pret_descrescator(lista)
		elif optiune == "8":
			ui_sume_preturi_fiecare_nume(lista)
		elif optiune == "a":
			show_all(lista)
		elif optiune == "x":
			break
		else:
			print("Optiune invalida!")
