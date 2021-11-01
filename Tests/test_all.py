from Tests.test_CRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare
from Tests.test_domain import test_rezervare
from Tests.test_functionalitati import test_clasa_superioara_dupa_nume, test_ieftinire_checkin, \
    test_pret_maxim_fiecare_clasa, test_ordonare_pret_descrescator, test_sume_preturi_fiecare_nume


def run_all_tests():
    test_rezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_clasa_superioara_dupa_nume()
    test_ieftinire_checkin()
    test_pret_maxim_fiecare_clasa()
    test_ordonare_pret_descrescator()
    test_sume_preturi_fiecare_nume()
