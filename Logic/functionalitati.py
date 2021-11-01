from Domain.rezervare import get_nume, creeaza_rezervare, get_id, get_pret, get_checkin, get_clasa


def clasa_superioara_dupa_nume(nume, lista):
	"""
	Trece toate rezervarile facute pe un nume dat la o clasa superioara data.
	:param nume: string
	:param lista: o lista de rezervari
	:return: lista cu rezervarile nemodificate si rezervarile modificate
	"""
	lista_noua = []
	for rezervare in lista:
		if nume == get_nume(rezervare):
			if get_clasa(rezervare) == "economy":
				clasa_superioara = "economy plus"
			else:
				clasa_superioara = "business"
			rezervare_noua = creeaza_rezervare(
				get_id(rezervare),
				get_nume(rezervare),
				clasa_superioara,
				get_pret(rezervare),
				get_checkin(rezervare)
				)
			lista_noua.append(rezervare_noua)
		else:
			lista_noua.append(rezervare)
	return lista_noua


def ieftinire_checkin(lista, procent):
	"""
	Reduce pretul tuturor rezervarilor la care s-a facut check-in cu un procentaj citit.
	:param lista: o lista cu rezervari
	:param procent: numar natural
	:return: lista cu rezervarile nemodificate si rezervarile modificate
	"""
	if procent < 0:
		raise ValueError("Procentajul trebuie sa fie un numar pozitiv!")
	lista_noua = []
	for rezervare in lista:
		if get_checkin(rezervare) == "da":
			rezervare_noua = creeaza_rezervare(
				get_id(rezervare),
				get_nume(rezervare),
				get_clasa(rezervare),
				get_pret(rezervare) - get_pret(rezervare) * procent / 100,
				"da"
				)
			lista_noua.append(rezervare_noua)
		else:
			lista_noua.append(rezervare)
	return lista_noua


def pret_maxim_fiecare_clasa(lista):
	"""
	Determina pretul maxim pentru fiecare clasa.
	:param lista: o lista cu rezervari
	:return: un dictionar continand pretul maxim pentru fiecare clasa
	"""
	rezultat = {}
	for rezervare in lista:
		clasa = get_clasa(rezervare)
		pret = get_pret(rezervare)
		if clasa in rezultat:
			if rezultat[clasa] < pret:
				rezultat[clasa] = pret
		else:
			rezultat[clasa] = pret
	return rezultat


def ordonare_pret_descrescator(lista):
	"""
	Ordoneaza rezervarile descrescator dupa pret.
	:param lista: o lista cu rezervari
	:return: lista ordonata descrescator dupa pret
	"""
	return sorted(lista, key=lambda rezervare: get_pret(rezervare), reverse=True)


def sume_preturi_fiecare_nume(lista):
	"""
	Afiseaza sumelor preturilor pentru fiecare nume.
	:param lista:
	:return:
	"""
	rezultat = {}
	for rezervare in lista:
		nume = get_nume(rezervare)
		if nume in rezultat:
			rezultat[nume] += get_pret(rezervare)
		else:
			rezultat[nume] = get_pret(rezervare)
	return rezultat
