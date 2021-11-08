from Domain.rezervare import get_clasa, get_pret, get_id
from Logic.CRUD import adauga_rezervare, get_by_id, sterge_rezervare
from Logic.functionalitati import clasa_superioara_dupa_nume, ieftinire_checkin, pret_maxim_fiecare_clasa, \
    ordonare_pret_descrescator, sume_preturi_fiecare_nume
from UI.console import undo, redo


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


def test_undo_redo():
    lista = []
    undo_operations = []
    redo_operations = []

    # add [ ] -> [1, 2, 3]
    lista = adauga_rezervare("1", "nume1", "economy plus", 1000, "da", lista)
    undo_operations.append([
        lambda: sterge_rezervare("1", lista),
        lambda: adauga_rezervare("1", "nume1", "economy plus", 1000, "da", lista)
    ])
    redo_operations.clear()
    lista = adauga_rezervare("2", "nume2", "economy plus", 2000, "nu", lista)
    undo_operations.append([
        lambda: sterge_rezervare("2", lista),
        lambda: adauga_rezervare("2", "nume2", "economy plus", 2000, "nu", lista)
    ])
    redo_operations.clear()
    lista = adauga_rezervare("3", "nume1", "business", 4000, "nu", lista)
    undo_operations.append([
        lambda: sterge_rezervare("3", lista),
        lambda: adauga_rezervare("3", "nume1", "business", 4000, "nu", lista)
    ])
    redo_operations.clear()

    # undo [1, 2, 3] -> [1, 2]
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    assert len(lista) == 2
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "2"

    # undo [1, 2] -> [1]
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"

    # undo [1] -> [ ]
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    assert len(lista) == 0

    # undo [ ] -> [ ]
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    assert len(lista) == 0

    # add [ ] -> 1, 2, 3
    lista = adauga_rezervare("1", "nume1", "economy plus", 1000, "da", lista)
    undo_operations.append([
        lambda: sterge_rezervare("1", lista),
        lambda: adauga_rezervare("1", "nume1", "economy plus", 1000, "da", lista)
    ])
    redo_operations.clear()
    lista = adauga_rezervare("2", "nume2", "economy plus", 2000, "nu", lista)
    undo_operations.append([
        lambda: sterge_rezervare("2", lista),
        lambda: adauga_rezervare("2", "nume2", "economy plus", 2000, "nu", lista)
    ])
    redo_operations.clear()
    lista = adauga_rezervare("3", "nume1", "business", 4000, "nu", lista)
    undo_operations.append([
        lambda: sterge_rezervare("3", lista),
        lambda: adauga_rezervare("3", "nume1", "business", 4000, "nu", lista)
    ])
    redo_operations.clear()

    # redo [1, 2, 3]  ->  [1, 2, 3]
    if redo_operations:
        lista = redo(undo_operations, redo_operations)
    assert len(lista) == 3
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "2"
    assert get_id(lista[2]) == "3"

    # undo x 2 [1, 2, 3] -> [1]
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"

    # redo [1]  ->  [1, 2]
    if redo_operations:
        lista = redo(undo_operations, redo_operations)
    assert len(lista) == 2
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "2"

    # redo [1, 2]  ->  [1, 2, 3]
    if redo_operations:
        lista = redo(undo_operations, redo_operations)
    assert len(lista) == 3
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "2"
    assert get_id(lista[2]) == "3"

    # undo x 2 [1, 2, 3] -> [1]
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"

    # add [1] -> [1, 4]
    lista = adauga_rezervare("4", "nume4", "economy plus", 1000, "da", lista)
    undo_operations.append([
        lambda: sterge_rezervare("4", lista),
        lambda: adauga_rezervare("4", "nume4", "economy plus", 1000, "da", lista)
    ])
    redo_operations.clear()
    assert len(lista) == 2
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "4"

    # redo [1, 4] -> [1, 4]
    if redo_operations:
        lista = redo(undo_operations, redo_operations)
    assert len(lista) == 2
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "4"

    # undo [1, 4] -> [1]
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    assert len(lista) == 1
    assert get_id(lista[0]) == "1"

    # undo [1] -> [ ]
    if undo_operations:
        lista = undo(undo_operations, redo_operations)
    assert len(lista) == 0

    # redo x 2 [ ] -> [1, 4]
    if redo_operations:
        lista = redo(undo_operations, redo_operations)
    if redo_operations:
        lista = redo(undo_operations, redo_operations)
    assert len(lista) == 2
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "4"

    # redo [1, 4] -> [1, 4]
    if redo_operations:
        lista = redo(undo_operations, redo_operations)
    assert len(lista) == 2
    assert get_id(lista[0]) == "1"
    assert get_id(lista[1]) == "4"
