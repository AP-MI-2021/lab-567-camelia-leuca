from Domain.rezervare import get_clasa
from Logic.CRUD import adauga_rezervare, get_by_id
from Logic.functionalitati import clasa_superioara_dupa_nume


def test_clasa_superioara_dupa_nume():
    lista = []
    lista = adauga_rezervare("1", "nume1", "economy", 4000, "da", lista)
    lista = adauga_rezervare("2", "nume1", "economy plus", 1000, "nu", lista)
    lista = adauga_rezervare("3", "nume3", "economy", 4000, "da", lista)
    lista = clasa_superioara_dupa_nume("nume1", lista)
    assert get_clasa(get_by_id("1", lista)) == "economy plus"
    assert get_clasa(get_by_id("2", lista)) == "business"
