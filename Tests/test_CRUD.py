from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare, get_by_id, sterge_rezervare, modifica_rezervare


def test_adauga_rezervare():
    lista = []
    lista = adauga_rezervare("1", "nume", "business", 4000, "da", lista)
    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "nume"
    assert get_clasa(get_by_id("1", lista)) == "business"
    assert get_pret(get_by_id("1", lista)) == 4000
    assert get_checkin(get_by_id("1", lista)) == "da"


def test_sterge_rezervare():
    lista = []
    lista = adauga_rezervare("1", "nume", "business", 4000, "da", lista)
    lista = adauga_rezervare("2", "Nume", "economy", 1000, "nu", lista)
    lista = sterge_rezervare("1", lista)
    lista = sterge_rezervare("3", lista)
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None


def test_modifica_rezervare():
    lista = []
    lista = adauga_rezervare("1", "nume", "business", 4000, "da", lista)
    lista = adauga_rezervare("2", "Nume", "economy", 1000, "nu", lista)

    lista = modifica_rezervare("2", "Nume", "business", 4000, "nu", lista)
    rezervare_updatata = get_by_id("2", lista)
    assert get_id(rezervare_updatata) == "2"
    assert get_nume(rezervare_updatata) == "Nume"
    assert get_clasa(rezervare_updatata) == "business"
    assert get_pret(rezervare_updatata) == 4000
    assert get_checkin(rezervare_updatata) == "nu"

    rezervare_neupdatata = get_by_id("1", lista)
    assert get_id(rezervare_neupdatata) == "1"
    assert get_nume(rezervare_neupdatata) == "nume"
    assert get_clasa(rezervare_neupdatata) == "business"
    assert get_pret(rezervare_neupdatata) == 4000
    assert get_checkin(rezervare_neupdatata) == "da"
