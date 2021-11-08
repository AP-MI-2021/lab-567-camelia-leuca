from Tests.test_all import run_all_tests
from UI.comanda import comanda_meniu
from UI.console import run_menu


def main():
    run_all_tests()
    meniu = input("Meniu 1 sau meniu 2? ")
    if "1" in meniu:
        run_menu([])
    elif "2" in meniu:
        comanda_meniu([])
    else:
        print("Meniul ales nu exista!")


main()
