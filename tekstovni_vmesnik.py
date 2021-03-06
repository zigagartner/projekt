import model
import math
import racunalnik
import random

def izpis_zmage(igralec):
    return f"Igre je konec, zmagal je igralec {igralec}."

def zahtevaj_vnos(igralec):
    while True:
        try:
            vnos = int(input(f"Izbira igralec {igralec}. Izberite število med 0 in 6:"))
        except ValueError:
            print("Vnos ni mogoč.")
            continue
        if vnos < 0 or vnos > 6:
            print("Vnos ni mogoč.")
        else:
            break
    return vnos

def stevilo_igralcev():
    while True:
        try:
            vnos = int(input("Koliko igralcev želi igrati (1 ali 2)?:"))
        except ValueError:
            print("Izbrano število igralcev ni mogoče.")
            continue
        if vnos != 1 and vnos != 2:
            print("Izbrano število igralcev ni mogoče.")
        else:
            break
    return vnos
                      
def po_koncani_igri():
    izbira = str(input("Ali želite odigrati novo igro (da/ne)?"))
    if izbira == "ne":
        print("Zaključili ste z igranjem, želimo vam lep dan!")
    elif izbira == "da":
        zazeni_igro()
    else:
        print("Izbira ni mogoča")
        izbira = str(input("Ali želite odigrati novo igro (da/ne)?"))

def izpis_neodlocenega_izida(polje):
    if model.prosti_stolpci(polje) == []:
        print("Izid je neodločen!")
        po_koncani_igri()
    else:
        pass
    
    
    
def pozeni_vmesnik():
    igra = model.nova_igra()

    konec_igre = False
    poteza = random.choice([0, 1])
    print(igra.polje)
    while not konec_igre:
        izpis_neodlocenega_izida(igra.polje)
        if poteza % 2 != 0:
            stolpec = zahtevaj_vnos(1)
            if igra.ali_je_prostor(stolpec):
                vrsta = igra.vnos_izbire_v_vrstico(stolpec)
                igra.dodaj_v_polje(vrsta, stolpec, 1)
                if igra.zmagovalna_poteza(1):
                    print(izpis_zmage(1))
                    konec_igre = True   
                poteza += 1     
            else:
                print("V stolpcu ni prostora!")        
        else:
            stolpec = zahtevaj_vnos(2)
            if igra.ali_je_prostor(stolpec):
                vrsta = igra.vnos_izbire_v_vrstico(stolpec)
                igra.dodaj_v_polje(vrsta, stolpec, 2)
                if igra.zmagovalna_poteza(2):
                    print(izpis_zmage(2))
                    konec_igre = True
                poteza += 1
            else:
                print("V stolpcu ni prostora!")
        print(igra.polje)
        if konec_igre == True:
            po_koncani_igri()
        
        
def pozeni_vmesnik_racunalnik():
    igra = model.nova_igra()
    konec_igre = False
    print(igra.polje)
    poteza = random.choice([0, 1])
    while not konec_igre:
        izpis_neodlocenega_izida(igra.polje)
        polje = igra.polje
        if poteza % 2 != 0:
            stolpec = zahtevaj_vnos(1)
            if igra.ali_je_prostor(stolpec):
                vrsta = igra.vnos_izbire_v_vrstico(stolpec)
                igra.dodaj_v_polje(vrsta, stolpec, 1)
                poteza += 1
                if igra.zmagovalna_poteza(1):
                    print(izpis_zmage(1))
                    konec_igre = True
            else:
                print("V stolpcu ni prostora!")
            print(igra.polje)
        else:
            stolpec = racunalnik.najboljsa_poteza(polje, 2)
            if igra.ali_je_prostor(stolpec):
                vrsta = igra.vnos_izbire_v_vrstico(stolpec)
                igra.dodaj_v_polje(vrsta, stolpec, 2)
                if igra.zmagovalna_poteza(2):
                    print(izpis_zmage(2))
                    konec_igre = True
                print(f"Računalnik je izbral {stolpec}.")
                print(igra.polje)
                poteza += 1
        if konec_igre == True:
            po_koncani_igri()
     
def zazeni_igro():
    print("Dobrodošli v igri štiri v vrsto!")
    igralci = stevilo_igralcev()
    if igralci == 1:
        return pozeni_vmesnik_racunalnik()
    elif igralci == 2:
        return pozeni_vmesnik()

zazeni_igro()








