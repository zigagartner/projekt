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
        ocena -= 4
    return ocena

def oceni_polje(polje, kos):
    ocena = 0
    #Vodoravno
    for v in range(STEVILO_VRSTIC):
        vrstica_seznam = [int(i) for i in list(polje[v, :])]
        for s in range(STEVILO_STOLPCEV - 3):
            del_polja = vrstica_seznam[s:s + DOLZINA_DELA]
            ocena += oceni_del_polja(del_polja, kos)
    #Navpicno
    for s in range(STEVILO_STOLPCEV):
        stolpec_seznam = [int(i) for i in list(polje[:, s])]
        for v in range(STEVILO_VRSTIC - 3):
            del_polja = stolpec_seznam[v: v + DOLZINA_DELA]
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

def minimax(polje, globina, alfa, beta, MaxIgralca):
    vse_mozne_izbire = mozne_izbire(polje)
    je_koncno = koncno_stanje(polje)
    if globina == 0 or je_koncno:
        if je_koncno:
            if zmagovalna_poteza(polje, RACUNALNIK):
                return (None, 100000000000000)
            elif zmagovalna_poteza(polje, IGRALEC_1):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            return (None, oceni_polje(polje, RACUNALNIK))
    if MaxIgralca:
        vrednost = -math.inf
        stolp = random.choice(vse_mozne_izbire)
        for s in vse_mozne_izbire:
            vrstica = vnos_izbire_v_vrstico(polje, s)
            kopija_polja = polje.copy()
            dodaj_v_polje(kopija_polja, vrstica, s, RACUNALNIK)
            nova_ocena = minimax(kopija_polja, globina - 1, alfa, beta, False)[1]
            if nova_ocena > vrednost:
                vrednost = nova_ocena
                stolp = s
            alfa = max(alfa, vrednost)
            if alfa >= beta:
                break
        return stolp, vrednost
    else:
        vrednost = math.inf
        stolp = random.choice(vse_mozne_izbire)
        for s in vse_mozne_izbire:
            vrstica = vnos_izbire_v_vrstico(polje, s)
            kopija_polja = polje.copy()
            dodaj_v_polje(kopija_polja, vrstica, s, IGRALEC_1)
            nova_ocena = minimax(kopija_polja, globina - 1, alfa, beta, True)[1]
            if nova_ocena < vrednost:
                vrednost = nova_ocena 
                stolp = s
            beta = min(beta, vrednost)
            if alfa >= beta:
                break
        return stolp, vrednost
    
