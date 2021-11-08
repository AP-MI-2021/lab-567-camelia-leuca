from Domain.rezervare import to_string, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare, get_by_id
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
	print("u. Undo")
	print("r. Redo")
	print("a. Afisare rezervari.")
	print("x. Iesire.")


def ui_adauga_rezervare(lista, undo_operations, redo_operations):
	try:
		id = input("Dati id-ul: ")
		nume = input("Dati numele: ")
		clasa = input("Dati clasa: ")
		pret = float(input("Dati pretul: "))
		checkin = input("Dati check-in-ul: ")
		rezultat = adauga_rezervare(id, nume, clasa, pret, checkin, lista)
		undo_operations.append([
			lambda: sterge_rezervare(id, rezultat),
			lambda: adauga_rezervare(id, nume, clasa, pret, checkin, lista)
		])
		redo_operations.clear()
		return rezultat
	except ValueError as ve:
		print("Eroare {}".format(ve))
		return lista


def ui_sterge_rezervare(lista, undo_operations, redo_operations):
	try:
		id = input("Dati id-ul rezervarii de sters: ")
		rezultat = sterge_rezervare(id, lista)
		rezervare_de_sters = get_by_id(id, lista)
		undo_operations.append([
			lambda: adauga_rezervare(
				id,
				get_nume(rezervare_de_sters),
				get_clasa(rezervare_de_sters),
				get_pret(rezervare_de_sters),
				get_checkin(rezervare_de_sters),
				rezultat),
			lambda: sterge_rezervare(id, lista)
		])
		redo_operations.clear()
		return rezultat
	except ValueError as ve:
		print("Eroare {}".format(ve))
		return lista


def ui_modifica_rezervare(lista, undo_operations, redo_operations):
	try:
		id = input("Dati id-ul rezervarii de modificat: ")
		nume = input("Dati noul nume: ")
		clasa = input("Dati noua clasa: ")
		pret = float(input("Dati noul pret: "))
		checkin = input("Dati noul check-in: ")
		rezultat = modifica_rezervare(id, nume, clasa, pret, checkin, lista)
		rezervare_veche = get_by_id(id, lista)
		undo_operations.append([
			lambda: modifica_rezervare(
				id,
				get_nume(rezervare_veche),
				get_clasa(rezervare_veche),
				get_pret(rezervare_veche),
				get_checkin(rezervare_veche),
				rezultat),
			lambda: modifica_rezervare(id, nume, clasa, pret, checkin, lista)
		])
		redo_operations.clear()
		return rezultat
	except ValueError as ve:
		print("Eroare {}".format(ve))
		return lista


def ui_clasa_superioara_dupa_nume(lista, undo_operations, redo_operations):
	nume = input("Dati numele dupa care se va face modificarea: ")
	rezultat = clasa_superioara_dupa_nume(nume, lista)
	undo_operations.append([
		lambda: lista,
		lambda: rezultat
	])
	redo_operations.clear()
	return rezultat


def ui_ieftinire_checkin(lista, undo_operations, redo_operations):
	try:
		procent = float(input("Dati procentajul cu care se vor ieftini rezervarile: "))
		rezultat = ieftinire_checkin(lista, procent)
		undo_operations.append([
			lambda: lista,
			lambda: rezultat
		])
		redo_operations.clear()
		return rezultat
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


def undo(undo_operations, redo_operations):
	operations = undo_operations.pop()
	redo_operations.append(operations)
	return operations[0]()


def redo(undo_operations, redo_operations):
	operations = redo_operations.pop()
	undo_operations.append(operations)
	return operations[1]()


def run_menu(lista):
	undo_operations = []
	redo_operations = []
	while True:
		print_menu()
		optiune = input("Dati optiunea: ")
		if optiune == "1":
			lista = ui_adauga_rezervare(lista, undo_operations, redo_operations)
		elif optiune == "2":
			lista = ui_sterge_rezervare(lista, undo_operations, redo_operations)
		elif optiune == "3":
			lista = ui_modifica_rezervare(lista, undo_operations, redo_operations)
		elif optiune == "4":
			lista = ui_clasa_superioara_dupa_nume(lista, undo_operations, redo_operations)
		elif optiune == "5":
			lista = ui_ieftinire_checkin(lista, undo_operations, redo_operations)
		elif optiune == "6":
			ui_pret_maxim_fiecare_clasa(lista)
		elif optiune == "7":
			ui_ordonare_pret_descrescator(lista)
		elif optiune == "8":
			ui_sume_preturi_fiecare_nume(lista)
		elif optiune == "u":
			if len(undo_operations) > 0:
				lista = undo(undo_operations, redo_operations)
			else:
				print("Nu se poate face undo!")
		elif optiune == "r":
			if len(redo_operations) > 0:
				lista = redo(undo_operations, redo_operations)
			else:
				print("Nu se poate face redo!")
		elif optiune == "a":
			show_all(lista)
		elif optiune == "x":
			break
		else:
			print("Optiune invalida!")
