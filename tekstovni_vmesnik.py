import model

def izpis_zmage(igralec):
    return f"Zmagal je igralec {igralec}."

def zahtevaj_vnos(igralec):
    while True:
        try:
            vnos = int(input(f"Izbira igralec {igralec}. Izberite število med 0 in 6:"))
        except ValueError:
            print("Vnos ni mogoč")
            vnos = int(input(f"Izbira igralec {igralec}. Izberite število med 0 in 6:"))
        if vnos < 0 and vnos > 6:
            print("Vnos ni mogoč")
            vnos = int(input(f"Izbira igralec {igralec}. Izberite število med 0 in 6:"))
        else:
            break
    return vnos

def po_koncani_igri():
    izbira = str(input("Ali želite odigrati novo igro (da/ne)?"))
    if izbira == "ne":
        print("Igre je konec!")
    elif izbira == "da":
        pozeni_vmesnik()
    else:
        print("Izbira ni mogoča")
        izbira = str(input("Ali želite odigrati novo igro (da/ne)?"))
    
def pozeni_vmesnik():
    igra = model.nova_igra()
    konec_igre = False
    print(igra.polje)
    while not konec_igre:
        if igra.stevilo_poteze() % 2 != 0:
            stolpec = zahtevaj_vnos(1)
            if igra.ali_je_prostor(stolpec):
                vrsta = igra.vnos_izbire_v_vrstico(stolpec)
                igra.dodaj_v_polje(stolpec, vrsta, 1)
                if igra.zmagovalna_poteza(1):
                    print(izpis_zmage(1))
                    konec_igre = True                
        else:
            stolpec = zahtevaj_vnos(2)
            if igra.ali_je_prostor(stolpec):
                vrstica = igra.vnos_izbire_v_vrstico(stolpec)
                igra.dodaj_v_polje(stolpec, vrstica, 2)
                if igra.zmagovalna_poteza(2):
                    print(izpis_zmage(2))
                    konec_igre = True
        print(igra.polje)
        if konec_igre == True:
            po_koncani_igri()
        
        
        
pozeni_vmesnik()





