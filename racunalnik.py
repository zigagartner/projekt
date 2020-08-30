import math
import random
import model


IGRALEC_1 = 1
RACUNALNIK = 2
DOLZINA_DELA = 4
PRAZNO_POLJE = 0
STEVILO_VRSTIC = 6
STEVILO_STOLPCEV = 7


def zmagovalna_poteza(polje, kos):
    #Vodoravno
    for s in range(STEVILO_STOLPCEV - 3): 
        for v in range(STEVILO_VRSTIC):
            if polje[v][s] == kos and polje[v][s + 1] == kos and polje[v][s + 2] == kos and polje[v][s + 3] == kos:
                return True
    #Navpicno
    for s in range(STEVILO_STOLPCEV): 
        for v in range(STEVILO_VRSTIC - 3):
            if polje[v][s] == kos and polje[v + 1][s] == kos and polje[v + 2][s] == kos and polje[v + 3][s] == kos:
                return True
    #Posevno navzgor
    for s in range(STEVILO_STOLPCEV - 3):
        for v in range(3, STEVILO_VRSTIC):
            if polje[v][s] == kos and polje[v - 1][s + 1] == kos and polje[v - 2][s + 2] == kos and polje[v - 3][s + 3] == kos:
                return True
    #Posevno navzdol
    for s in range(STEVILO_STOLPCEV - 3):
        for v in range(STEVILO_VRSTIC - 3):
            if polje[v][s] == kos and polje[v + 1][s + 1] == kos and polje[v + 2][s + 2] == kos and polje[v + 3][s + 3] == kos:
                return True   
    
def mozne_izbire(polje):
    izbire = []
    for stolpec in range(STEVILO_STOLPCEV):
        if polje[0][stolpec] == 0:
            izbire.append(stolpec)
    return izbire

def koncno_stanje(polje):
    return zmagovalna_poteza(polje, IGRALEC_1) or zmagovalna_poteza(polje, RACUNALNIK) or len(mozne_izbire(polje)) == 0

def vnos_izbire_v_vrstico(polje, stolpec):
    proste_vrstice = []
    for vrstica in range(STEVILO_VRSTIC):
        if polje[vrstica][stolpec] == 0:
            proste_vrstice.append(vrstica)
            vrstica = max(proste_vrstice)
    return vrstica

def dodaj_v_polje(polje, vrstica, stolpec, kos):
    polje[vrstica][stolpec] = kos

def oceni_del_polja(del_polja, kos):
    ocena = 0
    kos_nasprotnika = IGRALEC_1
    if kos == IGRALEC_1:
        kos_nasprotnika = RACUNALNIK
    if del_polja.count(kos) == 4:
        ocena += 100
    elif del_polja.count(kos) == 3 and del_polja.count(PRAZNO_POLJE) == 1:
        ocena += 5
    elif del_polja.count(kos) == 2 and del_polja.count(PRAZNO_POLJE) == 2:
        ocena += 2
    elif del_polja.count(kos_nasprotnika) == 3 and del_polja.count(PRAZNO_POLJE) == 1:
        ocena -= 25
    return ocena

def najboljsa_poteza(polje, kos):
    izbire = mozne_izbire(polje)
    najboljsa_ocena = 0
    najboljsi_stolpec = random.choice(izbire)
    for stolpec in izbire:
        vrstica = vnos_izbire_v_vrstico(polje, stolpec)
        kopija = polje.copy()
        dodaj_v_polje(kopija, vrstica, stolpec, kos)
        ocena = oceni_polje(polje, kos)
        if ocena > najboljsa_ocena:
            najboljsa_ocena = ocena
            najboljsi_stolpec = stolpec
    return najboljsi_stolpec

def oceni_polje(polje, kos):
    ocena = 0
    #Vodoravno
    for v in range(STEVILO_VRSTIC):
        vrstica = [int(i) for i in list(polje[v, :])]
        for s in range(STEVILO_STOLPCEV - 3):
            del_polja = vrstica[s:s + DOLZINA_DELA]
            ocena += oceni_del_polja(del_polja, kos)
    #Navpicno
    for s in range(STEVILO_STOLPCEV):
        stolpec = [int(i) for i in list(polje[:, s])]
        for v in range(STEVILO_VRSTIC - 3):
            del_polja = stolpec[v: v + DOLZINA_DELA]
            ocena += oceni_del_polja(del_polja, kos)
    #Diagonalno navzgor
    for v in range(3, STEVILO_VRSTIC):
        for s in range(STEVILO_STOLPCEV - 3):
            del_polja =[polje[v - i][s + i] for i in range(DOLZINA_DELA)]
            ocena += oceni_del_polja(del_polja, kos)
    #Diagonalno navzdol
    for v in range(STEVILO_VRSTIC - 3):
        for s in range(STEVILO_STOLPCEV - 3):
            del_polja = [polje[v + i][s + i] for i in range(DOLZINA_DELA)]
            ocena += oceni_del_polja(del_polja, kos)
    #Oceni sredinski stolpec
    sredinski_stolpec = [int(i) for i in list(polje[:, STEVILO_STOLPCEV // 2])]
    stevilo_kosov_v_sredini = sredinski_stolpec.count(kos)
    ocena += stevilo_kosov_v_sredini * 3
    return ocena

