def creeaza_rezervare(id, nume, clasa, pret, checkin):
	"""
	Creeaza un o lista pentru o rezervare.
	:param id:string
	:param nume:string
	:param clasa:string
	:param pret:float
	:param checkin:string
	:return:un dictionar ce contine o rezervare
	"""
	rezervare = [id, nume, clasa, pret, checkin]
	return rezervare


def get_id(rezervare):
	"""
	Ia id-ul unei rezervari.
	:param rezervare: dictionar ce retine o rezervare
	:return: id-ul rezervarii
	"""
	return rezervare[0]


def get_nume(rezervare):
	"""
	Ia numele unei rezervari.
	:param rezervare: dictionar ce retine o rezervare
	:return: numele pe care este facuta rezervarea
	"""
	return rezervare[1]


def get_clasa(rezervare):
	"""
	Ia clasa unei rezervari.
	:param rezervare: dictionar ce retine o rezervare
	:return: clasa rezervarii
	"""
	return rezervare[2]


def get_pret(rezervare):
	"""
	Ia pretul unei rezervari.
	:param rezervare: dictionar ce retine o rezervare
	:return: pretul rezervarii
	"""
	return rezervare[3]


def get_checkin(rezervare):
	"""
	Ia check-in-ul unei rezervari.
	:param rezervare: dictionar ce retine o rezervare
	:return: check-in-ul rezervarii
	"""
	return rezervare[4]


def to_string(rezervare):
	return "Id:{}, Nume:{}, Clasa:{}, Pret:{}, Check-in:{}".format(
		get_id(rezervare),
		get_nume(rezervare),
		get_clasa(rezervare),
		get_pret(rezervare),
		get_checkin(rezervare)
		)
