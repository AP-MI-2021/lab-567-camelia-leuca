from Domain.rezervare import creeaza_rezervare, get_id, get_pret


def adauga_rezervare(id, nume, clasa, pret, checkin, lista):
	"""
	Adauga o rezervare intr-o lista.
	:param id: string
	:param nume: string
	:param clasa: string
	:param pret: float
	:param checkin: string
	:param lista: lista de rezervari
	:return: lista continand vechile rezervari si noua rezervare
	"""
	if get_by_id(id, lista) is not None:
		raise ValueError("Id-ul exista deja!")
	if pret < 0:
		raise ValueError("Pretul trebuie sa fie un numar pozitiv!")
	if nume is None:
		raise ValueError("Numele trebuie completat!")
	if checkin != "da" and checkin != "nu":
		raise ValueError("Check-in-ul trebuie completat cu da sau nu!")
	if clasa != "economy" and clasa != "economy plus" and clasa != "business":
		raise ValueError("Clasa data nu exista!")
	rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
	return lista + [rezervare]


def get_by_id(id, lista):
	"""
	Da elementul din lista cu id-ul dat.
	:param id: string
	:param lista: lista de rezervari
	:return: rezervarea cu id-ul dat sau None daca nu exista
	"""
	for rezervare in lista:
		if get_id(rezervare) == id:
			return rezervare
	return None


def sterge_rezervare(id, lista):
	"""
	Sterge elementul cu id-ul dat dintr-o lista.
	:param id: string
	:param lista: lista de rezervari
	:return:
	"""
	if get_by_id(id, lista) is None:
		raise ValueError("Id-ul dat nu exista!")
	return [rezervare for rezervare in lista if get_id(rezervare) != id]


def modifica_rezervare(id, nume, clasa, pret, checkin, lista):
	"""
	Modifica o rezervare dintr-o lista.
	:param id: string
	:param nume: string
	:param clasa: string
	:param pret: float
	:param checkin: string
	:param lista: lista de rezervari
	:return: lista modificata
	"""
	if get_by_id(id, lista) is None:
		raise ValueError("Id-ul dat nu exista!")
	if pret < 0:
		raise ValueError("Pretul trebuie sa fie un numar pozitiv!")
	if nume is None:
		raise ValueError("Numele trebuie completat!")
	if checkin != "da" and checkin != "nu":
		raise ValueError("Check-in-ul trebuie completat cu da sau nu!")
	if clasa != "economy" and clasa != "economy plus" and clasa != "business":
		raise ValueError("Clasa data nu exista!")
	lista_noua = []
	for rezervare in lista:
		if get_id(rezervare) == id:
			rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, checkin)
			lista_noua.append(rezervare_noua)
		else:
			lista_noua.append(rezervare)
	return lista_noua
