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
