from Domain.rezervare import get_clasa, get_pret, get_id
from Logic.CRUD import adauga_rezervare, get_by_id
from Logic.functionalitati import clasa_superioara_dupa_nume, ieftinire_checkin, pret_maxim_fiecare_clasa, \
    ordonare_pret_descrescator, sume_preturi_fiecare_nume


def test_clasa_superioara_dupa_nume():
    lista = []
    lista = adauga_rezervare("1", "nume1", "economy", 4000, "da", lista)
    lista = adauga_rezervare("2", "nume1", "economy plus", 1000, "nu", lista)
    lista = adauga_rezervare("3", "nume3", "economy", 4000, "da", lista)
    lista = clasa_superioara_dupa_nume("nume1", lista)
    assert get_clasa(get_by_id("1", lista)) == "economy plus"
    assert get_clasa(get_by_id("2", lista)) == "business"


def test_ieftinire_checkin():
    lista = []
    lista = adauga_rezervare("1", "nume1", "economy", 4000, "da", lista)
    lista = adauga_rezervare("2", "nume1", "economy plus", 1000, "nu", lista)
    lista = adauga_rezervare("3", "nume3", "economy", 4000, "nu", lista)
    lista = ieftinire_checkin(lista, 50)
    assert get_pret(get_by_id("1", lista)) == 2000
    assert get_pret(get_by_id("2", lista)) == 1000
    assert get_pret(get_by_id("3", lista)) == 4000


def test_pret_maxim_fiecare_clasa():
    lista = []
    lista = adauga_rezervare("1", "nume1", "economy plus", 1000, "da", lista)
    lista = adauga_rezervare("2", "nume1", "economy plus", 2000, "nu", lista)
    lista = adauga_rezervare("3", "nume3", "business", 4000, "nu", lista)
    rezultat = pret_maxim_fiecare_clasa(lista)
    assert len(rezultat) == 2
    assert rezultat["economy plus"] == 2000
    assert rezultat["business"] == 4000


def test_ordonare_pret_descrescator():
    lista = []
    lista = adauga_rezervare("1", "nume1", "economy plus", 1000, "da", lista)
    lista = adauga_rezervare("2", "nume1", "economy plus", 2000, "nu", lista)
    lista = adauga_rezervare("3", "nume3", "business", 4000, "nu", lista)
    rezultat = ordonare_pret_descrescator(lista)
    assert get_id(rezultat[0]) == "3"
    assert get_id(rezultat[1]) == "2"
    assert get_id(rezultat[2]) == "1"


def test_sume_preturi_fiecare_nume():
    lista = []
    lista = adauga_rezervare("1", "nume1", "economy plus", 1000, "da", lista)
    lista = adauga_rezervare("2", "nume2", "economy plus", 2000, "nu", lista)
    lista = adauga_rezervare("3", "nume1", "business", 4000, "nu", lista)
    rezultat = sume_preturi_fiecare_nume(lista)
    assert len(rezultat) == 2
    assert rezultat["nume1"] == 5000
    assert rezultat["nume2"] == 2000
