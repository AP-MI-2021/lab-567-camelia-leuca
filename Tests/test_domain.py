from Domain.rezervare import creeaza_rezervare, get_id, get_nume, get_clasa, get_pret, get_checkin


def test_rezervare():
	rezervare = creeaza_rezervare("1", "nume", "business", 4000, "da")
	assert get_id(rezervare) == "1"
	assert get_nume(rezervare) == "nume"
	assert get_clasa(rezervare) == "business"
	assert get_pret(rezervare) == 4000
	assert get_checkin(rezervare) == "da"
